import datetime

# Bugünün tarihini al
trh1 = datetime.date.today()
# Yarın için tarih hesapla
trh2 = trh1 + datetime.timedelta(days=1)
print(trh1, trh2)

# Tarih farkını hesapla ve mutlak değerini al
fark = trh1 - trh2
fark = fark.days
fark = abs(fark)
print(fark)
