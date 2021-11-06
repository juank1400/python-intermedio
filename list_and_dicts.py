def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Juan", "lastname": "Cepeda"}

    super_list = [
        {"firstname": "Juan", "lastname": "Cepeda"},
        {"firstname": "Andres", "lastname": "Montenegro"},
        {"firstname": "Juliana", "lastname": "Gutierrez"},
        {"firstname": "Adriana", "lastname": "Rodriguez"},
        {"firstname": "German", "lastname": "Dominguez"},
        {"firstname": "Ricardo", "lastname": "Santos"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "squares": [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
        "cubes": [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000],
    }

    for key, value in super_dict.items():
        print(f"{key}: {value}")

    for item in super_list:
        print(item["firstname"], item["lastname"])

if __name__ == '__main__':
    run()
