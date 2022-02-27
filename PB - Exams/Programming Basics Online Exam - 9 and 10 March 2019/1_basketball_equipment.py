year_tax_basketball = int(input())

sneakers_price = year_tax_basketball - (year_tax_basketball * 0.40)
gear = sneakers_price - (sneakers_price * 0.20)
ball = gear / 4
accesories = ball / 5

total = year_tax_basketball + sneakers_price + gear + ball + accesories

print(f"{total:.2f}")
