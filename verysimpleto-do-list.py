import datetime
import time
import random



Gorevler = []
Gorev_sayisi = int(input('Kaç görev gireceksiniz : '))
esit_mi = True
i = 0
while esit_mi:
    for i in range(0,Gorev_sayisi+2):
        if i < Gorev_sayisi:
            Gorev_Gir = input('Bir görev giriniz : ')
            Gorevler.append(Gorev_Gir)
        elif i ==Gorev_sayisi:
            esit_mi = False
            break

