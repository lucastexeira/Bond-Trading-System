import math

class Bond:

    def __init__(self,notional,maturity,coupon,interest):

        self.notional = notional
        self.maturity = maturity
        self.coupon = coupon
        self.interest = interest
        self.frequency = 0.5

    def cashflows(self):
        numCashflows = int(self.matuarity / self.frequency)
        l = [ self.notional * self.coupon * self.frequency / 100.0 for i in range (numCashflows) ]
        l[-1] = l[-1] + self.notional
        return l

    def presentValues(self):
        ''' today's values of the cashflows '''
        presentValues = []
        for i, cashflow in enumerate(self.cashflows(), 1):
            presentValues.append(cashflow / math.pow(1 + interest, frequency * i))
        return presentValues

    def price(self):
        ''' in $100 USD '''
        return sum(self.presentValues()) / self.notional * 100.0 
