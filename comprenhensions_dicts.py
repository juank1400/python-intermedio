def run():
    numbers = {x: x**3 for x in range(1, 101) if x % 3 != 0}
    print(numbers)

if __name__ == '__main__':
    run()