import model.Period
from model.Period import Period
class PeriodsFactory:
    
    periods = []
    
    def __init__ (self):
        self.periods.append(Period(1,22,26,0,0)) 
        self.periods.append(Period(2,12,15,0,0))
        self.periods.append(Period(3,18,22,0,0))
        self.periods.append(Period(4,23,26,0,0))
        self.periods.append(Period(5,0,0,20,22))

    def getPeriods(self):
        return self.periods
    def desc(self):
        desc = ""
        for i in self.periods :
            desc += i.description() + "\n"
        return desc