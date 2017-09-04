from collections import defaultdict


class School(object):
    def __init__(self, schoolname):
        self.schoolname = schoolname
        self._grades = defaultdict(set)

    def grade(self, n):
        return self._grades[n]

    def add(self, name, grade):
        self._grades[grade].update({name})

    def sort(self):
        return [(g, tuple(sorted(self._grades[g])))
                for g in sorted(self._grades)]
