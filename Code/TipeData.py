#int: Python mengartikan urutan digit desimal tanpa awalan sebagai angka desimal:
print(10)
print(type(10))

# float: Secara opsional, karakter e atau E yang diikuti dengan bilangan bulat positif atau negatif dapat ditambahkan untuk menentukan notasi ilmiah:
print(4.2)
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)
# e = nol, "-" jumlah nol sebelum int

# string
print("Hacktiv8 x Inalum")
print(type("Hacktiv8 x Inalum"))

# boolean: true/false
print(type(True))
print(type(False))

# Variable Assignment:Untuk membuat variabel, Anda hanya perlu memberikan nilai dan mulai menggunakannya. Penugasan dilakukan dengan tanda sama dengan (=):
n =  300
print(n)
n = 1000
print(n)
n
# Python juga memungkinkan penugasan berantai, yang memungkinkan untuk menetapkan nilai yang sama ke beberapa variabel secara bersamaan:
a = b = c = 300
print(a,b,c)

# variable types :  variables are statically typed. That means a variable is initially declared to have a specific data type, and any value assigned to it during its lifetime must always have that type.
var = 23.5
print(var)

var = "semoga jago ngoding"
print(var)

name = 'adjie'
age = 21
has_laptop = True
print(name,age,has_laptop)

# Lowercase and uppercase letters are not the same. Use of the underscore character is significant as well. Each of the following defines a different variable:

age = 1
Age = 2
aGe = 3
a_g_e = 4
_age = 5
print(age,Age,aGe,a_g_e,_age)

# Camel Case: Second and subsequent words are capitalized, to make word boundaries easier to see. (Presumably, it struck someone at some point that the capital letters strewn throughout the variable name vaguely resemble camel humps.)
# Example: numberOfCollegeGraduates

# Pascal Case: Identical to Camel Case, except the first word is also capitalized.
# Example: NumberOfCollegeGraduates

# Snake Case: Words are separated by underscores.
# Example: number_of_college_graduates

# OPERATORS AND EXPRESSION
# The values that an operator acts on are called operands.
a = 10
b = 2
a + b

# kalimat yang didalam ada tanda kutip
print('Dia berkata "halo dek, kuliah apa kerja" ')