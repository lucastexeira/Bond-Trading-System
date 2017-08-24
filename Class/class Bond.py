import math
import scipy.optimize

class Bond:

    def __init__(self,notional,maturity,coupon,interest, quotedPrice):

        self.notional = notional
        self.maturity = maturity
        self.coupon = coupon
        self.interest = interest
        self.frequency = 0.5
        self.quotedPrice = quotedPrice

    def cashflows(self):
        numCashflows = int(self.matuarity / self.frequency)
        l = [ self.notional * self.coupon * self.frequency / 100.0 for i in range (numCashflows) ]
        l[-1] = l[-1] + self.notional
        return l

    def presentValues(self, bondYield = None):
        ''' today's values of the cashflows '''
        if not bondYield:
            bondYield = self.interest
        presentValues = []
        for i, cashflow in enumerate(self.cashflows(), 1):
            presentValues.append(cashflow / math.pow(1 + bondYield, self.frequency * i))
        return presentValues

    def price(self, bondYield = None):
        ''' in $100 USD '''
        return sum(self.presentValues(bondYield)) / self.notional * 100.0 

    def __g__(self, bondYield = None):
        diff = self.price(bondYield) - self.quotedPrice
        return diff

    def bondYield(self):
        ''' ... root-finding to find yield (which is the interest rate) from quoted price '''
        by = scipy.optimize.bisect(self.__g__,0.000000000001,0.999999999999, maxiter = 100, full_output = false)
        return by
