num1 = float(input("Number1?"))
num2 = float(input("Number 2?"))
op = input("Operator? Choose between +, -, * and /")

def main():
    x = 2.0
    y = 4.0

    print(f"{x} + {y} = {add(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


if __name__ == '__main__':
    main()
