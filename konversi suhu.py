print("cara konversi suhu")
print("konversi suhu celcius ke fahrenheit, kelvin, dan reamur")
print(" berikut hasilnya")
suhu = ("fahrenheit", "kelvin", "reamur")
suhu_celcius = float(input("masukan suhu dalam celcius"))
suhu_fahrenheit = (9./5) * suhu_celcius+32
suhu_kelvin = suhu_celcius + 273
suhu_reamur = (4./5) * suhu_celcius

print(suhu)

print("hasil perhitungan konversi suhu:")

print("1. suhu fahrenheit adalah: %f" %(suhu_fahrenheit))

print("2. suhu kelvin adalah: %f" %(suhu_kelvin))

print("3. suhu reamur adalah: %f" %(suhu_reamur))