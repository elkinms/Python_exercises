# 1. Find digits_sum(number)
#    Ex: number = 375 -> 5 + 7 + 3 = 15 return 15


def digits_sum(number):
    sum = 0
    rem = 0
    if number < 0:
        number = - number
    while number != 0:
        rem = number % 10
        sum += rem
        number = number // 10
    return sum


result = digits_sum(375)
print("result is", result)
print()


# 2.  print_number_column(number). Only positives
#     Ex: number = 3450
#     print:
#     3
#     4
#     5
#     0


def print_number_column(number):
    count = len(str(number))
    while count != 0:
        res = number // 10 ** (count - 1)
        print(res)
        number = number % 10 ** (count - 1)
        count -= 1


print_number_column(3450)
print()


# 3.  has_number(number, subnumber)
#     Ex: number = 344567    subnumber = 45   return True


def has_number(number, subnumber):
    if number < 0:
        number = -number
    size_num = len(str(number))
    size_sub = len(str(subnumber))
    if size_num < size_sub:
        return False
    i = size_num
    while i > 0:
        num = number % 10 ** (size_sub)
        if num == subnumber:
            return True
        number = number // 10
        i -= 1
    return False


res = has_number(344567, 45)
print(res)
print()


# 4. find max element in array
#    Ex: arr = [3, 3.14, -1, 0, 66, 13, 6.2]
#    Return 66

def max_array_element(arr):
    max_el = arr[0]
    for x in arr:
        if x > max_el:
            max_el = x
    return max_el


arr = [3, 3.14, -1, 0, 66, 13, 6.2]
res = max_array_element(arr)
print(res)
print()


# 5 find min prime number greater than given number
#   Ex: 1000000. Return 1000003

def is_prime(number):         # function checking if number is prime or not.
    if number % 2 == 0:
        return False
    div = 3                   # divisor
    num = int(number ** 0.5)  # SQR from number
    while div < num:
        if number % div == 0:
            return False
        div += 2
    return True


def find_prime_above(n):
    if n <= 0:
        print("Enter positive integer")
        return
    candidate = n + 1
    while not is_prime(candidate):  # while is_prime(candidate) != True:
        candidate += 1
    return candidate


result = find_prime_above(1000000)
print(result)





