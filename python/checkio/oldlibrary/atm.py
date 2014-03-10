def checkio(balance, withdrawal):
    for transaction in withdrawal:
        if (transaction + 1) <= balance and transaction % 5 == 0 and transaction > 0:
            balance -= (transaction + 1)
    return balance

checkio(100, [20, 20, 20, 20])
