deposit = float(input())
deposit_term_in_months = int(input())
yaerly_percent = float(input()) / 100

sum_deposit = deposit + deposit_term_in_months * ((deposit * yaerly_percent) / 12)

print(sum_deposit)




#
# a = float(input())
# b = int(input())
# c = float(input())/100
# interest = a * c
# m_interest = interest / 12
# total = a + (m_interest * b)
# print(total)