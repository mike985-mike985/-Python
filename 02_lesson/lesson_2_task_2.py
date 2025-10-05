def is_year_leap(number):

    return False if number % 4 == 0 else True


num_year = int(input("Введите число: "))

result = is_year_leap(num_year)

print(f"год {num_year} - {result}")
