# DIFFERENCE
class MySet:
    def __init__(self):
        self.data = []

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def difference(self, other):
        natija = MySet()

        for item in self.data:
            if item not in other.data:
                natija.add(item)

        return natija

    def show(self):
        print(self.data)

s1 = MySet()
s1.data = [1, 2, 3, 4]

s2 = MySet()
s2.data = [3, 4, 5]

s3 = s1.difference(s2)

s3.show()  
