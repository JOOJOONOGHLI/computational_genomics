from math import comb

def factorial(p):
    if p == 0:
        return 1
    else:
        return p * factorial(p-1)
def main():
    initial_factorial = factorial(26)
    running_total = 0
    print(initial_factorial)
    #generates initial factorial
    for j in range(27):
        c_term = comb(26, j)
        current_factorial= factorial(26-j)
        if j % 2 == 0:
            running_total = running_total - (current_factorial * c_term)
        else:
            running_total = running_total + current_factorial * c_term
    print(initial_factorial - running_total)

if __name__ == '__main__':
    main()