from math import exp, log
from datetime import datetime

def rate(purchasePrice, latestPrice, purchaseDateDMY, latestDateDMY, qty=1):
    """Compute annualized rate given buy/sale prices and dates.
    Counts 365 days in one year.

    rate(PV, FV, buyDate ("d/m/y"), sellDate, qty=1)

    qty affects FV price only."""
    
    latestDate = datetime.strptime(latestDateDMY, "%d/%m/%y")
    purchaseDate = datetime.strptime(purchaseDateDMY, "%d/%m/%y")
    daysDiff = (latestDate - purchaseDate).days
    if daysDiff <= 0:
        return "N/A"
        
    fv = float(latestPrice)
    pv = float(purchasePrice) / float(qty)
    
    # to get yearly equivalent, take exp(r) and subtract 1
    compoundRate = log(fv / pv) / (daysDiff / 365)
    return "{:.2f}%".format(100 * (exp(compoundRate) - 1))

def fv(pv, ratePerPeriod, numPeriods):
    """Future value with discrete compounding, given present value,
    rate per period, and number of periods."""
    
    return pv * (1 + ratePerPeriod) ** numPeriods

def cc(pv, ratePerPeriod, numPeriods):
    """Continuous compounding."""
    return exp(ratePerPeriod * numPeriods)
