class School():
    def __init__(self, name, grade = 0):
        self.name = name
        self.roster = {}
        self.grade = grade
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self):
        roster_sort = sorted(self.roster, key = lambda x: x.grade, reverse=True)
        for c in roster_sort:
            print(c.grade, c.name)
            
            