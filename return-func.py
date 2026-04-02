# def is_even(number = 8):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"
# print(is_even(4))  # Output: Juft
# print(is_even())   # Output: Juft
# result = is_even(7)
# print(result)  # Output: Toq


# Ternary operator yordamida yuqoridagi funksiyani qisqartirish mumkin:
from email.mime import text
from itertools import count


def is_even(number):
    return "Juft" if number % 2 == 0 else "Toq"

print(is_even(4))  # Output: Juft
print(is_even(7))  # Output: Toq

vowels = ['a', 'e', 'i', 'o', 'u']
def count_vowels(text):
     count = 0
     for char in text:
          if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]:
               count += 1
     return count
    
print(count_vowels("frontender"))
print(count_vowels("javascript"))

#s string boyicha for lopp ishlatish
# text = "Hello"
# for char in text:
#     print(char)