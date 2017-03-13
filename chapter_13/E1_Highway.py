class HighwayTraffic(object):
    __templates = [
        "Traffic alert: on the {highway} from {start} to {exit} is a jam about {length}.",
        "There was a traffic jam reported on the {highway} from {start} to {exit}."
    ]

    def __init__(self, highway, exit, start, length=0):
        self.highway = highway
        self.exit = exit
        self.start = start
        self.length = length

    def getMessage(self):
        if self.length:
            return self.__templates[0].format(highway=self.highway, start=self.start, exit=self.exit,
                                              length=self.length)
        else:
            return self.__templates[1].format(highway=self.highway, start=self.start, exit=self.exit)

    def __str__(self):
        return self.getMessage()


# Main Part
trafficJams = [("A1", "Bern", "Thun", "4km"), ("Route 66", "Ohio", "Orlando")]

for jam in trafficJams:
    print(str(HighwayTraffic(*jam)))
