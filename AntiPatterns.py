from collections import defaultdict
from typing import Dict, List
from Utils import clean_location_class, clean_location_function


class CommitVersion:
    def __init__(self, name, commit, date):
        self.name = name
        self.commit = commit
        self.date = date
        self.antiPatterns: Dict[str, List[AntiPattern]] = defaultdict(list)

    def __str__(self):
        return "{0} {1} {2}".format(self.commit, self.date, self.antiPatterns)

    __repr__ = __str__

    def ap_by_class(self, location):
        res = []
        for key, value in self.antiPatterns.items():
            for ap in value:
                if clean_location_class(ap.location) == location:
                    res.append([key, ap.location])
        return res

    def ap_by_function(self, location):
        res = []
        for key, value in self.antiPatterns.items():
            for ap in value:
                if clean_location_function(ap.location) == location:
                    res.append([key, ap.location])
        return res


class AntiPattern:
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return "{0}".format(self.location)

    __repr__ = __str__
