def fibonacci(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
while True:
    n = int(input("Ingrese un numero: "))
    
    if(n >= 1):
        break
    
for i in range(n):
    print(fibonacci(i))