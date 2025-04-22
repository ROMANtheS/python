
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
garden_set = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',}
meadow_set = {'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',}
print (set.union(garden_set, meadow_set))
print (set.intersection(garden_set,  meadow_set))
print (set.difference(garden_set, meadow_set))
print (set.difference(meadow_set, garden_set))
