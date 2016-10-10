class gbv_exchange(object):
    def __init__(self, tktValue, stksym):
        self.ticketValue = tktValue
        self.stksym = stksym
        self.stockdict = {'TEA':{'type':'common', 'last_dividend':0,'Par_value':100},
                          'POP':{'type':'common', 'last_dividend':8,'Par_value':100},
                          'ALE':{'type':'common', 'last_dividend':23,'Par_value':60},
                          'GIN':{'type':'preferred','last_dividend':8,'fixed_dividend':0.02,'Par_value':100},
                          'JOE':{'type':'common','last_dividend':13,'Par_value':250}}


    def getDividend(self):
        if self.stockdict[self.stksym]['type'] == 'common':
            print self.stockdict[self.stksym]['last_dividend'], self.ticketValue 
            commn_divid = self.stockdict[self.stksym]['last_dividend']/self.ticketValue
            return commn_divid
        if self.stockdict[self.stksym]['type'] == 'preferred':
            prfd_divid = self.stockdict[self.stksym]['Par_value']/self.ticketValue
            return prfd_divid

        
    def getpeRatio(self):
        dvdValue = self.getDividend()
        result =0.0
        if dvdValue >0 :
            peratio = self.ticketValue/dvdValue
            return peratio
        return result
 

    #def geomean(self, num_list):
       # return (num_list) ** (1.0/len(num_list))


    def geomean(self, value):
        val = 1
        for i in value:
            val = val * i
        gm = (val) ** (1.0/len(value))
        return gm




    def listsum(self, trade, quantity):
        theSum = 0
        qsum = 0
        for i in quantity:
            qsum = qsum + i
        #print qsum
        new_list = []
        zipped = zip(trade, quantity)
        for item in zipped:
            new_list.append(item[0] * item[1])
            newsum = 0
            for i in new_list:
                newsum = newsum + i
        #print newsum
        StockPrice = newsum / qsum
        print StockPrice
        return new_list   
    
  


     
gbvobj = gbv_exchange(7, 'POP')  
        
print gbvobj.getDividend()
print gbvobj.getpeRatio()
print gbvobj.geomean([5,6,7,8,9])
print gbvobj.listsum([10, 20, 30, 40, 50,60,70,80,90,100,110,120,130,140,150],[1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15])

