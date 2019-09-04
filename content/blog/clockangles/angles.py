import math

#constants
twoPi = 2.0*math.pi
maxDegree = 360.0
secondsInHour = 60
minutesInHour = secondsInHour
hoursInDay = 24
maxHour = math.ceil(hoursInDay/2)

# a simple clock class to do handle computation
class Clock():
    def __init__(self, hour, minute, radians):
        self.hour = hour
        self.minute = minute
        self.radians = radians
        self.factor = twoPi
        if not radians:
            self.factor = maxDegree
        
        self.validateTime()
    
    def validateTime(self):
        if self.hour > hoursInDay - 1 or self.hour < 0:
            raise ValueError('Time must be valid - check hours')
        
        if self.minute > minutesInHour - 1 or self.minute < 0:
            raise ValueError('Time must be valid - check minutes')
                        
    def __str__(self):
        return "Standard time is: {}, Time in minutes : {}, , Angle: {}".format( 
            self.getTimeStandardAsString(), 
            self.getTimeInMinutes(), 
            self.computeAngle())            
    
    def getTimeStandardAsString(self):
        timeInMinutes = self.getTimeInMinutes()
        hours = str(math.floor(timeInMinutes/minutesInHour))
        mins = str(timeInMinutes % minutesInHour)
    
        if len(hours) == 1:
            hours = "0" + hours
            
        if len(mins) == 1:
            mins = "0" + mins
            
        return hours + ":" + mins
    
    def getTimeInMinutes(self):
        return self.hour*minutesInHour + self.minute
    
    # every minute moves the minute hand by 6 degrees
    def computeMinuteAngle(self):
        return self.minute*self.factor/minutesInHour
    
    # every hour moves the hour hand by 30 degrees and each minute moves the hour hand by 0.5 degrees
    def computeHourAngle(self):
        # convert to non 24 hour (between 0 and 12 only)
        simpleTimeHour = self.hour
        if simpleTimeHour > maxHour:
            simpleTimeHour = simpleTimeHour - maxHour
    
        return (simpleTimeHour*self.factor + self.computeMinuteAngle())/maxHour
        
    def computeSmallAngle(self):
        minuteAngle = self.computeMinuteAngle()
        hourAngle = self.computeHourAngle()
    
        angle = abs(hourAngle - minuteAngle)
        
        return min(angle, abs(self.factor - angle))
    
    def computeLargeAngle(self):
        return self.factor - self.computeSmallAngle()
    
    def computeAngle(self):
        return self.computeSmallAngle()
    

clock = Clock(16,34, False)
print(clock)
