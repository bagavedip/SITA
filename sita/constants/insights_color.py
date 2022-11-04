import random


class ColorMap:
    """
     ColorMap function is used to map
     color in donut chart of
     insights all layers.
    """

    @staticmethod
    def get_color(layer_filter, key):
        Entity = {
            "1": "#808080",
            "10": "#373737",
            "11": "#594D58",
            "3": "#322D31",
            "4": "#696880",
            "5": "#ADADC9",
            "6": "#59515E",
            "7": "#3E3D53",
            "8": "#41424C",
            "9": "#564C4D",
            "2": "#4D4C5C"
        }

        Location = {
            "1": "#c3ac77",
            "10": "#d9aa3e",
            "2": "#504222",
            "3": "#a59673",
            "4": "#e7b031",
            "5": "#af8119",
            "6": "#b39041",
            "7": "#d9b76b",
            "8": "#f3e5c7",
            "9": "#d59814"
        }
        
        Assets = {
            "1": "#76a3cb",
            "10": "#6396c4",
            "11": "#518abd",
            "12": "#437db1",
            "13": "#3c709f",
            "2": "#35638c",
            "3": "#2e567a",
            "4": "#16447a",
            "5": "#4386b1",
            "6": "#437db1",
            "7": "#4374b1",
            "8": "#4c87bb",
            "9": "#5a90c1"
        }

        UseCase = {
            "1": "#3d55ad",
            "12": "#414f83",
            "13": "#7380ad",
            "15": "#3554bf",
            "16": "#7a90db",
            "17": "#3556c9",
            "19": "#08102e",
            "20": "#273156",
            "2": "#526ccd",
            "4": "#162354",
            "8": "#5c78df",
            "9": "#263d91"
        }

        Function = {
            "1": "#e6ffe6",
            "12": "#b3ffb3",
            "13": "#ccffcc",
            "15": "#99ff99",
            "16": "#80ff80",
            "17": "#66ff66",
            "19": "#4dff4d",
            "20": "#33ff33",
            "2": "#1aff1a",
            "4": "#00ff00",
            "8": "#00e600",
            "9": "#00cc00"
        }

        Criticality = {
            "2. Alta": "#b72a35",
            "3. Media": "#f0ae0c",
            "4. Baja": "#25ba3c"
        }

        if layer_filter == 'Entity':
            return random.choice(list(Entity.values()))
        elif layer_filter == 'Location':
            return random.choice(list(Location.values()))
        elif layer_filter == 'Assets':
            return random.choice(list(Assets.values()))
        elif layer_filter == 'UseCase':
            return random.choice(list(UseCase.values()))
        elif layer_filter == 'Function':
            return random.choice(list(Function.values()))
        elif layer_filter == 'Criticality' or layer_filter == 'Severity':
            return Criticality.get(key)
