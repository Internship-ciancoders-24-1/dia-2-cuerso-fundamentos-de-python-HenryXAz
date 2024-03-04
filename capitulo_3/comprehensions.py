import random

#  nos permiten generar secuencias a partir de otras secuencias

#  list comprehension
lista_numeros = list(range(100))
pares = [numero for numero in lista_numeros if numero % 2 ==0]
print(pares)

# dict comprehension
student_uid = [1,2,3]
students = ['Juan', 'Jose', 'Larsen']
students_with_uid = {uid:student for uid, student in zip(student_uid, students)}
print(students_with_uid)

# set comprehension
random_numbers = []

for number in range(10):
    random_numbers.append(random.randint(1,2))

none_repeated = {number for number in random_numbers}
print(none_repeated)