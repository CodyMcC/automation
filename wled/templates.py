

class Peaks:

    def __init__(self, flats: dict, peaks: dict):
        self.peaks_settings = peaks
        self.flats_settings = flats

        self.peaks = [
            {"start": 675, "stop": 790, "n": "Entry Peak - L", "rev": False, "set": 1},
            {"start": 790, "stop": 907, "n": "Entry Peak - R", "rev": True, "set": 1},
            {"start": 1229, "stop": 1369, "n": "R Peak - L", "rev": False, "set": 1},
            {"start": 1369, "stop": 1506, "n": "R Peak - L", "rev": True, "set": 1},
            {"start": 1832, "stop": 2026, "n": "L Peak - L", "rev": False, "set": 1},
            {"start": 2027, "stop": 2061, "n": "L Peak - R", "rev": True, "set": 1},
        ]
        self.flats = [
            {"start": 0, "stop": 299, "n": "Garage - L", "rev": False, "set": 0},
            {"start": 299, "stop": 599, "n": "Garage - R", "rev": True, "set": 0},
            {"start": 599, "stop": 675, "n": "Entry - LB", "rev": False, "set": 0},
            {"start": 907, "stop": 1010, "n": "Entry - RB", "rev": True, "set": 0},
            {"start": 1010, "stop": 1196, "n": "Entry - Living Room", "rev": True, "set": 0},
            {"start": 1509, "stop": 1544, "n": "R Peak - RB", "rev": True, "set": 0},
            {"start": 1544, "stop": 1735, "n": "R Peak - Office", "rev": True, "set": 0},
            {"start": 1735, "stop": 1832, "n": "L Peak - Flat", "rev": False, "set": 0},
            {"start": 1813, "stop": 1832, "n": "L Peak - Back", "rev": False, "set": 0},

        ]
        self.config = {
            "on": True,
            "bri": 255,
            "transition": 7,
            "mainseg": 0,
            "seg": []}
        self.generate_peaks()
        self.generate_flats()

    def generate_peaks(self):
        for peak in self.peaks:
            peak.update(self.peaks_settings)
            self.config['seg'].append(peak)

    def generate_flats(self):
        for flat in self.flats:
            flat.update(self.flats_settings)
            self.config['seg'].append(flat)


# {"on":true,"bri":128,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":2065,"grp":1,"spc":0,"of":0,"on":true,"frz":false,"bri":255,"cct":127,"set":0,"n":"","col":[[8,255,0],[0,0,0],[255,255,255]],"fx":90,"sx":128,"ix":128,"pal":5,"c1":128,"c2":128,"c3":16,"sel":true,"rev":false,"mi":false,"o1":false,"o2":false,"o3":false,"si":0,"m12":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}


peaks = {
        "on": True,
        "bri": 255,
        "transition": 7,
        "mainseg": 0,
        "seg": [{
                "id": 0,
                "start": 0,
                "stop": 299,
                "on": True,
                "bri": 255,
                "set": 1,
                "n": "Garage Left",
                "col": [
                    [
                        255,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ],
                "fx": 102,
                "sx": 96,
                "ix": 224,
                "c1": 128,
                "c2": 128,
                "c3": 16,
                "rev": False,
                "o1": False,
                "o2": False,
                "o3": False,
                "si": 0,
                # "m12": 1
            },
            {
                "id": 1,
                "start": 299,
                "stop": 599,
                "on": True,
                "bri": 255,
                "set": 0,
                "n": "Garage Right",
                "col": [
                    [
                        255,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ],
                "fx": 102,
                "sx": 96,
                "ix": 224,
                "c1": 128,
                "c2": 128,
                "c3": 16,
                "rev": True,
                "o1": False,
                "o2": False,
                "o3": False,
                "si": 0,
                # "m12": 0
            },
{
                "id": 3,
                "start": 675,
                "stop": 790,
                "on": True,
                "bri": 255,
                "set": 0,
                "n": "Entry Peak (L)",
                "col": [
                    [
                        255,
                        170,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ],
                "fx": 28,
                "sx": 128,
                "ix": 128,
                "c1": 128,
                "c2": 128,
                "c3": 16,
                "rev": False,
                "o1": False,
                "o2": False,
                "o3": False,
                "si": 0,
                # "m12": 0
            },
            {
                "id": 4,
                "start": 790,
                "stop": 907,
                "on": True,
                "bri": 255,
                "set": 0,
                "n": "Entry Peak (R)",
                "col": [
                    [
                        255,
                        170,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ],
                    [
                        0,
                        0,
                        0
                    ]
                ],
                "fx": 28,
                "sx": 128,
                "ix": 128,
                "c1": 128,
                "c2": 128,
                "c3": 16,
                "rev": True,
                "o1": False,
                "o2": False,
                "o3": False,
                "si": 0,
                # "m12": 0
            },
        ]}


effects = {'Solid': 0, 'Blink': 1, 'Breathe': 2, 'Wipe': 3, 'Wipe Random': 4, 'Random Colors': 5, 'Sweep': 6, 'Dynamic': 7, 'Colorloop': 8, 'Rainbow': 9, 'Scan': 10, 'Dual Scan': 11, 'Fade': 12, 'Chase': 28, 'Chase Rainbow': 30, 'Running': 15, 'Saw': 16, 'Twinkle': 17, 'Dissolve': 18, 'Dissolve Rnd': 19, 'Sparkle': 20, 'Dark Sparkle': 21, 'Sparkle+': 22, 'Strobe': 23, 'Strobe Rainbow': 24, 'Mega Strobe': 25, 'Blink Rainbow': 26, 'Android': 27, 'Chase Random': 29, 'Chase Flash': 31, 'Chase Flash Rnd': 32, 'Rainbow Runner': 33, 'Colorful': 34, 'Traffic Light': 35, 'Sweep Random': 36, 'Running 2': 37, 'Red & Blue': 38, 'Stream': 39, 'Scanner': 40, 'Lighthouse': 41, 'Fireworks': 42, 'Rain': 43, 'Merry Christmas': 44, 'Fire Flicker': 45, 'Gradient': 46, 'Loading': 47, 'In Out': 48, 'In In': 49, 'Out Out': 50, 'Out In': 51, 'Circus': 52, 'Halloween': 53, 'Tri Chase': 54, 'Tri Wipe': 55, 'Tri Fade': 56, 'Lightning': 57, 'ICU': 58, 'Multi Comet': 59, 'Dual Scanner': 60, 'Stream 2': 61, 'Oscillate': 62, 'Pride 2015': 63, 'Juggle': 64, 'Palette': 65, 'Fire 2012': 66, 'Colorwaves': 67, 'BPM': 68, 'Fill Noise': 69, 'Noise 1': 70, 'Noise 2': 71, 'Noise 3': 72, 'Noise 4': 73, 'Colortwinkle': 74, 'Lake': 75, 'Meteor': 76, 'Smooth Meteor': 77, 'Railway': 78, 'Ripple': 79}
effects = {'Solid': 0, 'Blink': 1, 'Breathe': 2, 'Wipe': 3, 'Wipe Random': 4, 'Random Colors': 5, 'Sweep': 6, 'Dynamic': 7, 'Colorloop': 8, 'Rainbow': 9, 'Scan': 10, 'Scan Dual': 11, 'Fade': 12, 'Theater': 13, 'Theater Rainbow': 14, 'Running': 15, 'Saw': 16, 'Twinkle': 17, 'Dissolve': 18, 'Dissolve Rnd': 19, 'Sparkle': 20, 'Sparkle Dark': 21, 'Sparkle+': 22, 'Strobe': 23, 'Strobe Rainbow': 24, 'Strobe Mega': 25, 'Blink Rainbow': 26, 'Android': 27, 'Chase': 28, 'Chase Random': 29, 'Chase Rainbow': 30, 'Chase Flash': 31, 'Chase Flash Rnd': 32, 'Rainbow Runner': 33, 'Colorful': 34, 'Traffic Light': 35, 'Sweep Random': 36, 'Chase 2': 37, 'Aurora': 38, 'Stream': 39, 'Scanner': 40, 'Lighthouse': 41, 'Fireworks': 42, 'Rain': 43, 'Tetrix': 44, 'Fire Flicker': 45, 'Gradient': 46, 'Loading': 47, 'Rolling Balls': 48, 'Fairy': 49, 'Two Dots': 50, 'Fairytwinkle': 51, 'Running Dual': 52, 'RSVD': 171, 'Chase 3': 54, 'Tri Wipe': 55, 'Tri Fade': 56, 'Lightning': 57, 'ICU': 58, 'Multi Comet': 59, 'Scanner Dual': 60, 'Stream 2': 61, 'Oscillate': 62, 'Pride 2015': 63, 'Juggle': 64, 'Palette': 65, 'Fire 2012': 66, 'Colorwaves': 67, 'Bpm': 68, 'Fill Noise': 69, 'Noise 1': 70, 'Noise 2': 71, 'Noise 3': 72, 'Noise 4': 73, 'Colortwinkles': 74, 'Lake': 75, 'Meteor': 76, 'Meteor Smooth': 77, 'Railway': 78, 'Ripple': 79, 'Twinklefox': 80, 'Twinklecat': 81, 'Halloween Eyes': 82, 'Solid Pattern': 83, 'Solid Pattern Tri': 84, 'Spots': 85, 'Spots Fade': 86, 'Glitter': 87, 'Candle': 88, 'Fireworks Starburst': 89, 'Fireworks 1D': 90, 'Bouncing Balls': 91, 'Sinelon': 92, 'Sinelon Dual': 93, 'Sinelon Rainbow': 94, 'Popcorn': 95, 'Drip': 96, 'Plasma': 97, 'Percent': 98, 'Ripple Rainbow': 99, 'Heartbeat': 100, 'Pacifica': 101, 'Candle Multi': 102, 'Solid Glitter': 103, 'Sunrise': 104, 'Phased': 105, 'Twinkleup': 106, 'Noise Pal': 107, 'Sine': 108, 'Phased Noise': 109, 'Flow': 110, 'Chunchun': 111, 'Dancing Shadows': 112, 'Washing Machine': 113, 'Blends': 115, 'TV Simulator': 116, 'Dynamic Smooth': 117, 'Spaceships': 118, 'Crazy Bees': 119, 'Ghost Rider': 120, 'Blobs': 121, 'Scrolling Text': 122, 'Drift Rose': 123, 'Distortion Waves': 124, 'Soap': 125, 'Octopus': 126, 'Waving Cell': 127, 'Pixels': 128, 'Pixelwave': 129, 'Juggles': 130, 'Matripix': 131, 'Gravimeter': 132, 'Plasmoid': 133, 'Puddles': 134, 'Midnoise': 135, 'Noisemeter': 136, 'Freqwave': 137, 'Freqmatrix': 138, 'GEQ': 139, 'Waterfall': 140, 'Freqpixels': 141, 'Noisefire': 143, 'Puddlepeak': 144, 'Noisemove': 145, 'Noise2D': 146, 'Perlin Move': 147, 'Ripple Peak': 148, 'Firenoise': 149, 'Squared Swirl': 150, 'DNA': 152, 'Matrix': 153, 'Metaballs': 154, 'Freqmap': 155, 'Gravcenter': 156, 'Gravcentric': 157, 'Gravfreq': 158, 'DJ Light': 159, 'Funky Plank': 160, 'Pulser': 162, 'Blurz': 163, 'Drift': 164, 'Waverly': 165, 'Sun Radiation': 166, 'Colored Bursts': 167, 'Julia': 168, 'Game Of Life': 172, 'Tartan': 173, 'Polar Lights': 174, 'Swirl': 175, 'Lissajous': 176, 'Frizzles': 177, 'Plasma Ball': 178, 'Flow Stripe': 179, 'Hiphotic': 180, 'Sindots': 181, 'DNA Spiral': 182, 'Black Hole': 183, 'Wavesins': 184, 'Rocktaves': 185, 'Akemi': 186}
