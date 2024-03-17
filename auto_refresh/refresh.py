# Can be run from cron to refresh at the top of the hour
from pynput.keyboard import Key, Controller
keyboard = Controller()


keyboard.press(Key.f5)
keyboard.release(Key.f5)
