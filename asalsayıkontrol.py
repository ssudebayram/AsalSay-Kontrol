print("sayı giriniz")
sayı1 = int (input())
p = 0
i = 2
while i<sayı1:
    if sayı1 == 0:
        p = 1
        break
    i = i+1

if p==0:
    print("\n" +str(sayı1)+ " sayısı asal sayıdır.")
else:
    print("\n" +str(sayı1)+ " sayısı asal sayı değildir.")
