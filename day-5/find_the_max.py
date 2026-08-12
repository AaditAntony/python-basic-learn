numbers = [1, 2, 3, 4, 5,200, 6, 7, 8, 9,123]

largest = numbers[0]

for number in numbers:
    if number >largest:
        largest =  number

print(f" the largest number is {largest}")