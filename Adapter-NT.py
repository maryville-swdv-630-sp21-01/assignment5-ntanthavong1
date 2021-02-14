import time
import datetime

class Employee():

    def __init__(self):
        pass

    def clockIn(self):
        self.timeIn = datetime.datetime.now()
        print(self.timeIn)
        return self.timeIn

    def clockOut(self):
        self.timeOut = datetime.datetime.now()
        print(self.timeOut)
        return self.timeOut

    def getHoursWorked(self, timeIn, timeOut):
        self.timeWorked = TimeAdapter(self.timeIn, self.timeOut)
        self.hoursWorked = (self.timeWorked.adaptTimeToSeconds() / 3600)
        return self.hoursWorked

class TimeAdapter():

    def __init__(self, timeIn, timeOut):
        self.timeOut = timeOut
        self.timeIn = timeIn
        self.timeWorked = self.timeOut - self.timeIn

    def adaptTimeToSeconds(self):
        timeWorkedInSeconds = self.timeWorked.total_seconds()
        return timeWorkedInSeconds # In seconds

bob = Employee()
timeIn = bob.clockIn()
time.sleep(5)
timeOut = bob.clockOut()
print(bob.getHoursWorked(timeIn, timeOut))

