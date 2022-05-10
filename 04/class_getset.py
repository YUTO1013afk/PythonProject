class Book:
    tax_rate = 0.1
    def __init__(self, unit_price):
        self.unit_price = unit_price
        self.discount = 0

    def get_discounts(self):
        return self.discount
    
    def set_discounts(self, val):
        if 0 <= val <= 100:
            self.discount = val
        else:
            raise ValueError("入力した値が間違っています")

    def price(self):
        return int(self.unit_price * (1 - self.discount / 100) * (1 + self.tax_rate))

#main
b1 = Book(1000) # 定価1000円の本
print(f'現在の値引率：{b1.get_discounts()}%')
b1.set_discounts(10) # 値引率 10%
print(f'現在の値引率：{b1.get_discounts()}%')
print(f'販売価格：{b1.price()}')
print('-='*30)

b2 = Book(2000) # 定価2000円の本
print(f'現在の値引率：{b2.get_discounts()}%')
b2.set_discounts(10) # 値引率 -10%
print(f'現在の値引率：{b2.get_discounts()}%')
print(f'販売価格：{b2.price()}')