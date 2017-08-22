class Bond:

    def __init__(self,notional,maturity,coupon,interest):

        self.notional = notional
        self.maturity = maturity
        self.coupon = coupon
        self.interest = interest

    def cashflows(self):
        numCashflows = int(self.matuarity / self.frecuency)
        l = [ self.notional * self.coupon * self.frecuency / 100.0 for i in range (numClashflows) ]
        l[-1] = l[-1] + self.notional
        return l

    def todayPriceCashflows(self):
        pass

    def price(self):
        return sum(self.todayPriceCashflows()) 
