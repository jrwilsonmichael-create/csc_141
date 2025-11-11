# I will add ordinal numbers
numbers = list(range(1, 20))
for numbers in numbers:
    if numbers == 1:
        print(f"{numbers}st")
    elif numbers == 2:
        print(f"{numbers}nd")
    elif numbers == 3:
        print(f"{numbers}rd")