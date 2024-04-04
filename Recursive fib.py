def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
x=int(input("Enter the number: "))

if x<0:
    print("Please enter a positive number...")
else:
    print("The sequence is :  ")
    for i in range(x+1):
        print(fibonacci(i))


    
