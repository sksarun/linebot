
from model.Period import Period
class PeriodsFactory:
    
    periods = []
    
    def __init__ (self):
        self.periods = []
        self.periods.append(Period('2020','Jan','22-Jan','26-Jan','','')) 
        self.periods.append(Period('2020','Feb','12-Feb','15-Feb','',''))
        self.periods.append(Period('2020','Mar','18-Mar','22-Mar','',''))
        self.periods.append(Period('2020','Apr','23-Apr','26-Apr','',''))
        self.periods.append(Period('2020','May','04-Jun','','20-May','22-May'))

    def getPeriods(self):
        return self.periods
    def desc(self):
        desc = ""
        for i in self.periods :
            desc += i.description() 
        return desc

#periodFac = PeriodsFactory()
#print(periodFac.desc())