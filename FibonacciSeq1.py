#By considering the terms in the Fibonacci Sequence, find the sum of even valued terms.
num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
fibonacci = [num1,num2]
max = int(input('Enter max number: '))
n = 2
while True :
    newfib = fibonacci[n-1] + fibonacci[n-2]
    if int(newfib) > max :
        break
    fibonacci.append(newfib)
    n = n + 1
print(fibonacci)

evennum = list()
for num in fibonacci :
    if num % 2 == 0 :
        evennum.append(num)

print(sum(evennum))
