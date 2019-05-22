import math  


class Geolocalisation:
    
    RAD_MILES = 3959
    RAD_KM = 6371

    @staticmethod
    def calculateRadius(self, x1, y1, x2, y2):
        radius = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
        return radius

    @staticmethod
    def convertDistanceIntoRadKM(self, distance):
        r = distance / RAD_KM
        return r

    @staticmethod
    def convertDistanceIntoRadMILES(self, distance):
        r = distance / RAD_MILES
        return r