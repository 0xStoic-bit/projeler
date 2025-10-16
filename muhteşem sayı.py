sayi = int(input('Bir sayı giriniz'))
toplam = 0
for i in range(1,sayi):
   if sayi %i ==0:
       toplam +=i
if toplam == sayi:
    print('Muhteşem sayı')
else:
    print('Muhteşem sayı değil')
