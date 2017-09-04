CHILDREN = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
PLANTS = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}


class Garden(object):
    def __init__(self, garden, students=CHILDREN):
        self.students = sorted(students)
        rows = garden.split()
        patches = [rows[0][i:i+2] + rows[1][i:i+2]
                   for i in range(0,2*len(self.students),2)]
        self._garden = {s: [PLANTS[ch] for ch in p]
                        for s, p in zip(self.students, patches)}

    def plants(self, student):
        return self._garden[student]
