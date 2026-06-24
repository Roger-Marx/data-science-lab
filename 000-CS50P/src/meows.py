#meows = 3
#
#for _ in range(meows):
#    print("meow")


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


animal_1 = Cat()
animal_1.meow()