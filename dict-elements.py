# Dictionary elementlari bilan ishlash
phone = {
    'brand' : 'Apple',
    'model' : 'iPhone 17 Pro Max',
    'year' : 2023,
    'color' : 'Phantom Gray',
}
#1. get metodi - kalit orqali qiymat olish
print(phone.get('model')) #iPhone 17 Pro Max
print(phone.get('price', "Narx topilmadi")) # 1500
print(phone.get('battery')) #None (Kalit mavjud emas)
print(phone.get('baterry', "Kalit topilmadi")) # Kalit topilmadi

#2. items() metodi - lug'at elementlarini (kalit-qiymat juftligini) olish
print(phone.items()) # dict_items([('brand', 'Apple'), ('model', 'iPhone 17 Pro Max'), ('year', 2023), ('color', 'Phantom Gray')])
for key, value in phone.items():
    print(f"{key}:{value}")

telefonlar = {
    'ali' : 'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}
for k , q in telefonlar.items() :
    # print(f"{k.title()}ning telefoni {q.title()}")

# 3.keys() metodi - lug'atning barcha kalitlarini olish
 print(phone.keys()) # dict_keys(['brand', 'model', 'year', 'color'])
print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = {
    'olma' : 10000,
    'banan' : 15000,
    'anor' : 20000
}
print("Do'konimizda quyidagi mahsulotlar bor:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori
# 1.listda in operatori qiymat mavjudligini tekshiradi
fruits = ['olma', 'banan', 'anor']
print('olma' in fruits) # True
print('uzum' in fruits) # False

fruit = input("Qaysi meva yoqadi? ")
if fruit in fruits:
    print(f"{fruit.title()} do'konimizda bor")
else:
    print(f"{fruit.title()} do'konimizda yo'q")

bozorlik = ['non', 'baliq', 'anor', 'uzum']
# for mahsulot in mahsulotlar:
#     print(mahsulot) #lug'atning kalitlari

#mahsulotlar - lugat , nbozorlik -ro'yxat , mahsulot - lug'atning kaliti
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

print(sorted(mahsulotlar.keys())) # ['anor', 'banan', 'olma']
print("Do'konimizda quyidagi mahsulotlar bor:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# 5 .values() metodi - lug'atning barcha qiymatlarini olish
print(phone.values()) # dict_values(['Apple', 'iPhone 17 Pro Max', 2023, 'Phantom Gray'])
print(telefonlar.values()) # dict_values(['iphone x', 'galaxy s9', 'mi 10 pro', 'nokia 3310'])

telefonlar = {
    'ali' : 'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}

print('Foydalanuvchilar quyidagi telefonlarga ega:')
for tel in telefonlar.values():
    print(tel.title())
