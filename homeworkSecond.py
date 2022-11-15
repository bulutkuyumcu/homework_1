sayi1 = int(input("ilk sayıy giriniz: "))
sayi2 = int(input("ikinci sayıyı giriniz: "))
toplam = 0

for i in range(sayi1,sayi2):
    if i % 2 == 1:
        continue
    toplam += i
print("{} sayısı ile {} sayısı arasındaki çift sayıların toplamı {} sayısıdır.".format(sayi1,sayi2,toplam))
