class Student:
    ...



def main() -> None:

    student = get_student()
    print(f'{student["name"]} from {student["house"]}')


def get_student() -> dict:
    student = Student()  # this makes student a variable of type Student instead of a dict as before
    student.name = input.("Name: ")  #student["name"] = input("Name: ")
    student.house =  = input("House: ") # student["house"] = input("House: ")
    #  variable student is an instance of the Class Student
    #  It has attributes (intenal variables or properties) .name and .house  
    #  those are connected to the each other by the instance it self, that is a Class
    return student


if __name__ == "__main__":
    main()
