from hash_distribution import plot, distribute
from string import printable

def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
        )

plot(distribute(printable, 6, hash_function))
