def factorial(num, show):
    from math import factorial
    if num < 0:
        print("Factorial of negative num does not exist")
    if show == True:
        cont = num
        for v in range(0, num):
            print(f'{cont}',end='')
            if cont != 1:
                print(' x ',end='')
            cont -= 1
    print(' = ',end='')
    print(factorial(num))

factorial(5, show=True)





