import math


class MyTime:
    seconds = 0
    def __init__(self, seconds):
        self.seconds = seconds

    def toTime(self):
        remain = self.seconds
        if(remain >= 3600):
            hours = math.floor(remain / 3600)
            remain %= hours * 3600
        else :
            hours = 0

        if(remain >= 60):
            minutes = math.floor(remain / 60)
            remain %= minutes * 60
        else: minutes = 0

        seconds = remain
        return "HH:mm:ss {}:{}:{}".format(hours, minutes, seconds)