# Data types (Ma'lumot turlari)
# 1.integer; 2. float; 3.string; 4. boolean; 5. list; 6. tuple; 7. distionary
cars = ['audi', 'chevrolet', 'BYD' , 'tesla']

# Dictionary (lug'at)
# key-value pair (kalit-qiymat juftligi)
car = {
 'brand': 'Ford',
 'name': 'Mustang',
 'year' : 2000,
 'color' : 'blue',
}
print(car)
print(type(car)) # <class 'dict' >


student = {
    'fullname' : 'John Doe',
    'age' : 20,
    'course' : 3,
    'favorite_books' : ['Atomic habits' , 'Otkan kunlar', 'Ikki eshik orasi'],
    'is_completed': False,
    'is_married': True
}

# 1. Qiymatlarni olish
print(student['fullname'])
print(student['age'])
print(student['favorite_books'])

for book in student['favorite_books'] :
    print(book)

# 2. Qiymatlarni o'zgartirish
student = ['age'] = 21
student['course' ] = 4
print(student)

# 3. Yangi key-value qo'shish
student['hobbies']= [ 'Reading a book', 'Watching a football match', 'Playing tennis']
print(student)

#4.Key-value ni o'chirish
del student ['is_married']
print(student)

#5. Emty dict (bo'sh lug'at)
talaba_1 = {}

talaba_1['ism'] = 'yulduz soporboyeva'
talaba_1['kurs']= 3
talaba_1['yosh'] = 15
print(talaba_1)
print(f" Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}- kurs")

#get() metodi
telefonlar = {
    'ali' : 'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}
print(telefonlar.get('vali'))
print(telefonlar.get(''))

#homework 1.
mam = {
    'name' : 'Nabira',
    'year' : '1990' ,
    'country' : 'Xorazm'
} 
print(f"Onamning ismi {mam['name']} , {mam['year']}-yilda, {mam['country']} viloyatida tug'ilgan.")
#homework 2.
taomlar = {
   'alisa': 'sushi' ,
    'leyla': 'pizza' ,
     'emma': 'Hamburger' ,
}
print(f"alisaning sevimli taomi{taomlar['alisa']}")
print(f"leylaning sevimli taomi{taomlar['leyla']}")
print(f"emmaning sevimli taomi{taomlar['emma']}")

