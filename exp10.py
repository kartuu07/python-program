def prime(n):
    if n <= 1:
        print("Not prime")
        return
    for i in range (2, n):
        if n % i == 0:
            print("not prime")
            return
    print("Prime")
num = int(input("Enter the Number: "))
prime(num)    
        
