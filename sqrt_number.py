import math as math

def run():
    numbers = {x: math.sqrt(x) for x in range(1, 101)}
    print(numbers)

if __name__ == '__main__':
    run()