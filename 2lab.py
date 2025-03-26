#первая задача
import itertools

def count_codes():
    letters = ['И', 'В', 'А', 'Н']
    total = 0
    for code in itertools.product(letters, repeat=5):
        if 'И' in code:
            total += 1
    return total

#вторая задача
def count_zeros_in_octal():
    expression = 7 * (512 ** 120) - 6 * (64 ** 100) + (8 ** 210) - 255
    octal = oct(expression)[2:]
    return octal.count('0')

#третья задача
def count_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
    return count
def find_number_with_max_divisors(start, end):
    max_divisors = -1
    result_number = start
    for num in range(start, end + 1):
        divisors = count_divisors(num)
        if divisors > max_divisors or (divisors == max_divisors and num < result_number):
            max_divisors = divisors
            result_number = num
    return (max_divisors, result_number)
print("Задача 1:", count_codes())
print("Задача 2:", count_zeros_in_octal())
print("Задача 3:", find_number_with_max_divisors(84052, 84130))