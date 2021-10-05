def recur_fibo(n):
    if n == 1:
           return 0
    elif n == 2:
       return 1
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def menu():
    n = int(input())
    for val in range(1, n+1):
        print(recur_fibo(val))

while True:
    menu()
