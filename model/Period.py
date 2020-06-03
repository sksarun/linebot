class Period:
    month = ''
    year = ''
    periodstart = ''
    periodend = ''
    ovulationstart = ''
    ovulationend = ''
    def __init__(self,y,m,ps,pe,os,oe):
        self.year = y
        self.month = m
        self.periodstart = ps
        self.periodend = pe
        self.ovulationstart = os
        self.ovulationend = oe

    def description(self):
        desc_str = "Year:%s Month:%s PeriodStart:%s PeriodEnd:%s OvulationStartdate:%s OvulationEnddate:%s \n"%(self.year,self.month,self.periodstart,self.periodend,self.ovulationstart,self.ovulationend)
        return desc_str
        