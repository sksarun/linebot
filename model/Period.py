class Period:
    month = 0
    periodstart = 0
    periodend = 0
    ovulationstart = 0
    ovulationend = 0
    def __init__(self,m,ps,pe,os,oe):
        self.month = m
        self.periodstart = ps
        self.periodend = pe
        self.ovulationstart = os
        self.ovulationend = oe

    def description(self):
        desc_str = "Month:%d PeriodStart:%d PeriodEnd:%d OvulationStartdate:%d OvulationEnddate:%d \n"%(self.month,self.periodstart,self.periodend,self.ovulationstart,self.ovulationend)
        return desc_str
        