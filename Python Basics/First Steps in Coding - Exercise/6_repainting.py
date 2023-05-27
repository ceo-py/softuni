nylon_amount_mt = int (input())
paint_amount_lt = int (input())
thinner_amount_lt = int (input())
hours = int (input())
amount_nylon = (nylon_amount_mt + 2) * 1.50
amount_paint = (paint_amount_lt * 1.1) * 14.50
amount_thinner = thinner_amount_lt * 5.00
amount_bags = 0.40
all_amount = amount_nylon + amount_paint + amount_thinner + amount_bags
amount_masters = (all_amount * 0.30) * hours
total_amount = all_amount + amount_masters
print(total_amount)






#
# neededNylon = int(input())
# neededPaint = int(input())
# thinner = int(input())
# hoursForBuliders = int(input())
#
# nylonPrice = (neededNylon + 2) * 1.50
# paintPrice = (neededPaint * 1.10) * 14.50
# thinnerPrice = thinner * 5
#
# totalSumMaterials = nylonPrice + paintPrice + thinnerPrice + 0.40
# buildersSum = (totalSumMaterials * 0.30) * hoursForBuliders
#
# totalSum = totalSumMaterials + buildersSum
#
# print(totalSum)
#
#
#
#




#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# aa = (a + 2) * 1.50
# bb = (b * 1.1) * 14.50
# cc = c * 5
# expense = aa + bb + cc + 0.40
# workers = (expense * 0.30) * d
# total = expense + workers
# print(total)
#
