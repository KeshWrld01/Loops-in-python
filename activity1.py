for i in range(1, 11):
    print(f"10 x {i} = {10*i}")

#start pattern
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for i in range(i):
        print("x ", end='')
    print()


#natural number sum
total_sum = sum(range(1, 11))
print(f"The sum of the first ten natural numbers is: {total_sum}")

#program to check if number is prime
num =int(input("Enter your number: "))
#check if number is greater than 1
if num>1:
    #loop only up to the square root of num for efficiency
    for i in range (2, int(num**0.5)+1):
        #if num is divisible by any number is not a prime
        if num&i==0:
            print("f{num} is not a prime number.")
            break
        #if no divisor was found, the number is prime
    else:
        print(f"{num} is a prime number.")
else:
    #Numbers less than 2 are not prime numbers
    print(f"{num} is not a prime number.")