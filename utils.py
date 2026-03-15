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
