MainNumber = 4679307774
num_len = len(str(MainNumber))

sum_of_numbers = 0
digit: str
for digit in str(MainNumber):
    sum_of_numbers += int(digit) ** num_len

if sum_of_numbers == MainNumber:
    message = 'TRUE: Number ' + str(MainNumber) + ' is an Armstrong Number.'
else:
    message = 'FALSE Number ' + str(MainNumber) + ' is NOT an Armstrong Number'
print(message)
