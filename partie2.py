class Student:
    def __init__(self, fname, lname, age, cne, average):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.cne = cne
        self.average = average
def main():
    list = []
    s1 = Student("anas", "zenagui", 21, L111111, 15)
    s2 = Student("ahmed", "bakkali", 21, L121212, 17)
    list.append(s1)
    list.append(s2)

    sorted_lists = sorted(list, key=lambda x: x.age)



