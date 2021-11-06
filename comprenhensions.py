def run():
    # Create a list of numbers that are divisible by 4, 6 and 9
    numbers = [x for x in range(1, 100000) if x % 4 == 0 and x % 6 == 0 and x % 9 == 0]
    print(numbers)

if __name__ == '__main__':
    run()