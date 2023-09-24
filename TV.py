"""
Uses HAP-python to turn a raspberry pi into a homekit TV that controls an actual TV via cec commands.
https://github.com/ikalchev/HAP-python
sudo apt-get install libavahi-compat-libdnssd-dev
pip3 install HAP-python[QRCode]
"""


from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_TELEVISION
import cec


class TV(Accessory):

    SOURCES = {
        'dashboard': 3,
        'HDMI 2': 3,
        'HDMI 3': 3,
    }

    def __init__(self, *args, **kwargs):
        super(TV, self).__init__(*args, **kwargs)
        cec.init()
        self.tv = cec.Device(cec.CECDEVICE_TV)
        self.category = CATEGORY_TELEVISION

        self.set_info_service(
            manufacturer='HaPK',
            model='Raspberry Pi',
            firmware_revision='1.0',
            serial_number='1'
        )

        tv_service = self.add_preload_service(
            'Television', ['Name',
                           'Active',
                           'ActiveIdentifier',
                           'RemoteKey',
                           'SleepDiscoveryMode',
                           ],
        )
        self._active = tv_service.configure_char(
            'Active', value=self._get_state(),
            setter_callback=self._on_active_changed,
            getter_callback=self._get_state
        )

        tv_service.configure_char(
            'ActiveIdentifier', value=1,
            setter_callback=self._on_active_identifier_changed,
        )
        tv_service.configure_char(
            'RemoteKey', setter_callback=self._on_remote_key,
        )

        tv_service.configure_char('SleepDiscoveryMode', value=1)

        for idx, (source_name, source_type) in enumerate(self.SOURCES.items()):
            input_source = self.add_preload_service('InputSource', ['Name', 'Identifier'])
            input_source.configure_char('Name', value=source_name)
            input_source.configure_char('Identifier', value=idx + 1)
            # TODO: implement persistence for ConfiguredName
            input_source.configure_char('ConfiguredName', value=source_name)
            input_source.configure_char('InputSourceType', value=source_type)
            input_source.configure_char('IsConfigured', value=1)
            input_source.configure_char('CurrentVisibilityState', value=0)

            tv_service.add_linked_service(input_source)

    @Accessory.run_at_interval(5)
    def run(self):
        state = self._get_state()  # Just grab it once, so we don't have to spam cec
        if state != self._active.value:
            print("values are out of sync")
            print(f"\tself._active = {self._active.value}")
            print(f"\tcec value = {state}")
            print()
            self._active.set_value(state)

    def _on_active_changed(self, value):
        self.tv.power_on() if value else self.tv.standby()
        print(f"Turn {'on' if value else 'off'}")

    def _get_state(self):
        return 1 if self.tv.is_on() else 0

    def remote(self, value):
        print(value)

    def _on_active_identifier_changed(self, value):
        if value == 1:
            cec.set_active_source(1)
        print('Change input to %s' % list(self.SOURCES.keys())[value-1])
        print(value)

    def _on_remote_key(self, value):
        print('Remote key %d pressed' % value)

    def _on_mute(self, value):
        print('Mute' if value else 'Unmute')

    def _on_volume_selector(self, value):
        print('%screase volume' % ('In' if value == 0 else 'De'))


def main():
    import logging
    import signal
    import time

    from pyhap.accessory_driver import AccessoryDriver

    logging.basicConfig(level=logging.INFO)

    while True:
        # Wait for the network to come up.
        try:
            driver = AccessoryDriver(port=51826, persist_file='/home/pi/.tv.state')
            break
        except OSError:
            time.sleep(5)
    
    accessory = TV(driver, 'TV')
    driver.add_accessory(accessory=accessory)

    signal.signal(signal.SIGTERM, driver.signal_handler)
    driver.start()


if __name__ == '__main__':
    main()
