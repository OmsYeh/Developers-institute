import pprint


class Farm:
    def __init__(self, farm_name):
        self.animal = {}
        self.farm_name = farm_name

    def add_animal(self, new_animal, count=1):
        lwrcs_ani = new_animal.lower()
        if lwrcs_ani in self.animal:
            self.animal[lwrcs_ani] += count
            pprint.pprint(f"You've added {count} {lwrcs_ani} to your collection")
        else:
            self.animal[lwrcs_ani] = count
            print(f"{self.farm_name}'s Farm: \n")
        for item, amount in self.animal.items():
            print("{} : {}".format(item, amount))

    @staticmethod
    def get_info():
        return " \n   E-I-E-I-O! \n"

    def get_animal_types(self):
        animal_list = list(self.animal.keys())
        print(animal_list)

    def get_short_info(self):
        animal_list = list(self.animal.keys())
        temp = []
        l1 = sorted(temp)
        for animal in animal_list:
            if animal != animal_list[-1]:
                l1.append(animal + ",")
            else:
                l1.append("and " + animal)
        l2 = " ".join(str(x) for x in l1)
        print(f"McDonald’s farm has {l2}.")


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_animal_types()
macdonald.get_short_info()

