import random


class ColorMap:
    """
    ColorMap function is used to map
    color in donut chart of
    OEI all layers.
    """

    @staticmethod
    def get_color(layer_filter, key):
        SLA = {
            " Alta": "#165B65",
            " Baja": "#16293A",
            " Media": "#437DB1",
        }

        value0 = {
            "false": "#B72A35",
            "true": "#1DBC36",
        }

        Category = {
            "1": "#2CB6C9",
            "10": "#54CADA",
            "11": "#2498AB",
            "12": "#64adb5",
            "13": "#595446",
            "2": "#1a47ba",
            "3": "#c9bfa1",
            "4": "#64adb5",
            "5": "#182526",
            "6": "#1a47ba",
            "7": "#1a47ba",
            "8": "#9da3b3",
            "9": "#27cc48",
            "0": "#27cc48"
        }

        Tickets = {
            "1": "#269147",
            "10": "#68a37a",
            "11": "#53b370",
            "12": "#1d4229",
            "13": "#1e6234",
            "2": "#4dcd76",
            "3": "#1e9945",
            "4": "#0b4a1f",
            "5": "#b5d9c1",
            "6": "#476451",
            "7": "#87cfa0",
            "8": "#86f5ad",
            "9": "#2cf171",
            "0": "#0fd354"
        }

        Status = {
            "Open": "#9DBD6F",
            "Closed": "#6E9537",
        }

        Priority = {
            "2. Alta": "#B72A35",
            "4. Baja": "#1DBC36",
            "3. Media": "#F0AE0c"
        }
        First_Response_Time = {
            "1": "#ffeee6",
            "10": "#ffddcc",
            "11": "#ffccb3",
            "12": "#ffbb99",
            "13": "#ffaa80",
            "2": "#ff9966",
            "3": "#ff884d",
            "4": "#ff7733",
            "5": "#ff661a",
            "6": "#ff5500",
            "7": "#e64d00",
            "8": "#cc4400",
            "9": "#b33c00",
            "0": "#993300"
        }

        Response_Time = {
            "1": "#fff7e6",
            "10": "#ffeecc",
            "11": "#ffe6b3",
            "12": "#ffdd99",
            "13": "#ffd480",
            "2": "#ffcc66",
            "3": "#ffc34d",
            "4": "#ffbb33",
            "5": "#ffb31a",
            "6": "#ffaa00",
            "7": "#e69900",
            "8": "#cc8800",
            "9": "#b37700",
            "0": "#805500"
        }

        False_Positives = {
            "1": "#f2e6ff",
            "10": "#e6ccff",
            "11": "#d9b3ff",
            "12": "#cc99ff",
            "13": "#bf80ff",
            "2": "#b366ff",
            "3": "#a64dff",
            "4": "#9933ff",
            "5": "#8c1aff",
            "6": "#8000ff",
            "7": "#330066",
            "8": "#26004d",
            "9": "#27cc48",
            "0": "#27cc48"
        }

        Reopened = {
            "1": "#ccddff",
            "10": "#b3ccff",
            "11": "#99bbff",
            "12": "#80aaff",
            "13": "#6699ff",
            "2": "#4d88ff",
            "3": "#3377ff",
            "4": "#003399",
            "5": "#003cb3",
            "6": "#002b80",
            "7": "#002266",
            "8": "#001a4d",
            "9": "#0044cc",
            "0": "#0055ff"
        }

        value1 = {
            "0": "#B72A35",
            "1": "#1DBC36",
        }

        value2 = {
            "0": "#B72A35",
            "1": "#1DBC36",
        }

        value3 = {
            "0": "#B72A35",
            "1": "#1DBC36",
        }

        if layer_filter == 'SLA':
            return SLA.get(key)
        elif layer_filter == 'value0':
            return value0.get(key)
        elif layer_filter == 'value1':
            return value1.get(key)
        elif layer_filter == 'value2':
            return value2.get(key)
        elif layer_filter == 'value3':
            return value3.get(key)
        elif layer_filter == 'Status':
            return Status.get(key)
        elif layer_filter == 'Priority':
            return Priority.get(key)
        elif layer_filter == 'Category':
            return random.choice(list(Category.values()))
        elif layer_filter == 'Tickets':
            return random.choice(list(Tickets.values()))
        elif layer_filter == 'False_Positives':
            return random.choice(list(False_Positives.values()))
        elif layer_filter == 'First_Response_Time':
            return random.choice(list(First_Response_Time.values()))
        elif layer_filter == 'Response_Time':
            return random.choice(list(Response_Time.values()))
        elif layer_filter == 'Reopened':
            return random.choice(list(Reopened.values()))


