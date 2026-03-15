from utils import gcd, fibonacci, is_power_of_five, dot_product, heron_area

print('НСД чисел 48 і 18:', gcd(48, 18))
print('10-те число Фібоначчі:', fibonacci(10))
print('Чи є 125 степенем п\'ятірки?', is_power_of_five(125))
print('Скалярний добуток [1, 2, 3] та [4, 5, 6]:', dot_product([1, 2, 3], [4, 5, 6]))
print('Площа трикутника (3, 4, 5):', heron_area(3, 4, 5))
