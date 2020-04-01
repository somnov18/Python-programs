def is_prime(num):
    
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: 
        print(num,'is prime!')

num=int(input("Enter a no.: "))
is_prime(num)