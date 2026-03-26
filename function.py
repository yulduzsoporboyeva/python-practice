#Function - ma'lum bir vazifani bajaruvchi kod bloklari
#Funksiya yaratish uchun def kalit so'zidan foydalanamiz
#Pythondagi tayyor funksiyalar - print(), input(), len(), sorted() va boshqalar
print("Hello World")
#Funksiyani e'lon qilish(declaration) va chaqirish(call)
def salom_ber():
    print("Salom, dunyo!")

#Funksiyani chaqirish(call)
salom_ber() # Salom, dunyo!

#Funksiyada argumentlar va parametrlar
def salom_ber(ism):
    print(f"Salom, {ism}!")

salom_ber("Ali") # Salom, Ali!
salom_ber("Vali") # Salom, Vali!

def yigindi(a, b):
    print(a + b)

yigindi(5, 10) # 15
yigindi(3, 7) # 10

def calculate_age(birth_year = 2011, name = "Yulduz"):
    age = 2026 - birth_year
    print(f"{name}ning yoshi {age} da")

calculate_age(2011, "Yulduz")

def yosh_hisobla(tugilgan_yil, joriy_yil = 2026):
    print(f"Sizning yoshingiz {joriy_yil - tugilgan_yil} da")
yosh_hisobla(2011)