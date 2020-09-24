def getMoneySpent(keyboards, drives, b):
    allPrices = list()
    for kprice in keyboards:
        for dprice in drives:
            allPrices.append(kprice + dprice)
    outSpend = [i for i in allPrices if i <= b]
    if outSpend == []:
        return -1
    else:
        return max(outSpend)

# HackerRank practice challenge : https://www.hackerrank.com/challenges/electronics-shop/problem

moneyOutput = getMoneySpent([10,2,3],[3,1],5)
print(moneyOutput)