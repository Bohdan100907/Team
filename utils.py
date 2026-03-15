def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def is_prime(n):
    Перевіряє, чи є число простим.
    if n <= 1:
        return False
    # Перевіряємо дільники від 2 до кореня з n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):
    '''Знаходить найбільший спільний дільник двох чисел.'''
    while b != 0:
        a, b = b, a % b
    return a
def fibonacci(n):
    '''Повертає n-те число Фібоначчі.'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def is_power_of_five(n):
    '''Перевіряє, чи є число степенем п'ятірки.'''
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1
def dot_product(v1, v2):
    '''Обчислює скалярний добуток двох векторів однакової довжини.'''
    if len(v1) != len(v2):
        return None
    return sum(x * y for x, y in zip(v1, v2))
def heron_area(a, b, c):
    '''Обчислює площу трикутника за трьома сторонами.'''
    if a + b <= c or a + c <= b or b + c <= a:
        return None 
    
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return round(area, 2)
