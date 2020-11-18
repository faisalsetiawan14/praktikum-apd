print("----------perulangan---------")

N = int(input("masukan nilai :"))
for x in range(N):
    if(10 ** x > N):
        break
    else:
        print("hasil perulangannya adalah :")
    print("nilai yang terkecil dari 10^x lebih dari N adalah", 10 ** x)