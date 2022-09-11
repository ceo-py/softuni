a = int(input()) * 10.35
b = int(input()) * 12.40
c = int(input()) * 8.15

m_total = a + b + c
d_price = m_total * 0.20
total = m_total + d_price + 2.50
print(float("{:.2f}".format(total)))