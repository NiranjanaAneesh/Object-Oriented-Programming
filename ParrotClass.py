class Parrot:
    species = "bird"
    def __init__(self, name , age):
        self.name = name
        self.age = age
Lillie = Parrot("Lillie",3)
Millie = Parrot("Millie",7)
print("Lillie is a {}".format(Lillie.species))
print("Millie is also a {}".format(Millie.species))
print("{} is {} years old".format(Lillie.name , Lillie .age))
print("{} is {} years old".format(Millie.name , Millie .age))
        