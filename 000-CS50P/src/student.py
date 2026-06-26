def main() -> None:
    # name:str = get_name()
    # house:str = get_house()
    student = get_student()
    # if student[0] == "Padma":
    #     student[1] = 'Ravenclaw'
        
    print(f'{student["name"]} from {student["house"]}')


# def get_name() -> str:
#     return input("Name: ")


# def get_house() -> str:
#     return input("House:")

def get_student() -> dict:
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()

