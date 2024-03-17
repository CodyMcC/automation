import requests
from wled.templates import effects, Peaks

wled_house = "http://192.168.1.63/json"

peaks_settings = {
                    'on': True,
                    'fx': effects['Fireworks 1D'],
                    'ix': 0,
                    'col': [[8, 255, 0], [0, 0, 0], [255, 255, 255]],
                    "pal": 5,
}
flats_settings = {
                    'on': True,
                    'fx': effects['Chase 2'],
                    'ix': 255,
                    'col': [[0, 255, 0], [255, 255, 255]],
}
peaks = Peaks(flats_settings, peaks_settings)


response = requests.post(wled_house, json=peaks.config)
print(response.status_code)
print(response.json())

