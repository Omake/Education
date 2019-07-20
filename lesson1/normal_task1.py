originalNumber = 58975
max = 0


while originalNumber!=0:
    partNumber = originalNumber % 10
    if partNumber > max:
        max = partNumber
    originalNumber = originalNumber // 10

print("Максимальная цифра в числе: ",max)
