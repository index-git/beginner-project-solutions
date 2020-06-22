MainNumber = 4679307774
NumLen = len(str(MainNumber))

SumNumber = 0
Digit: str
for Digit in str(MainNumber):
    SumNumber += int(Digit)**NumLen

Msg = 'TRUE: Number '+str(MainNumber)+' is an Armstrong Number.' if SumNumber == MainNumber else 'FALSE Number '+str(MainNumber)+' is NOT an Armstrong Number'
print(Msg)
