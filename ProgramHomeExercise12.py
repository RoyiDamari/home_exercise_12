# Exercise 1
oscar_winners: set[str] = {"Leonardo Dicaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                           "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};
# a
oscar_winners.add("Emma Watson");
print(oscar_winners);

# b
oscar_winners.clear();
print(oscar_winners);

# c
oscar_winners: set[str] = {"Leonardo Dicaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                           "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};

oscar_winners1 = oscar_winners.copy();
print(oscar_winners1);

# d
oscar_winners.remove("Meryl Streep");
print(oscar_winners);

# e
titanic_actors: set[str] = {"Leonardo Dicaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"};
dark_knight_actors: set[str] = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman",
                                "Aaron Eckhart"};

print(titanic_actors.intersection(dark_knight_actors));

# f
iron_man_actors: set[str] = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"};
avengers_actors: set[str] = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
                             "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"};

print(iron_man_actors & avengers_actors);

# g
actor_list: set[str] = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
                        "Leonardo Dicaprio", "Tom Hanks"};
print(actor_list.issubset(oscar_winners));

# h
print(actor_list.issuperset(avengers_actors));

# i
movie_cast: set[str] = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"};
elem = movie_cast.pop();
print(movie_cast);

# j
movie_cast.discard('Will Smith');
print(movie_cast);

# k
print(titanic_actors.difference(oscar_winners));

# l
print(titanic_actors.symmetric_difference(dark_knight_actors));

# m
oscar_winners.update(["Cate Blanchett", "Daniel Day-Lewis"]);
print(oscar_winners);

# n
print(titanic_actors.union(dark_knight_actors));

# o
dark_knight_rises_actors: set[str] = {"Christian Bale", "Michael Caine", "Gary Oldman",
                                      "Tom Hardy", "Joseph Gordon-Levitt"};

print(dark_knight_actors < dark_knight_rises_actors);

# p
legendary_actors: set[str] = {"Al Pacino", "Robert De Niro", "Marlon Brando",
                              "Jack Nicholson", "Dustin Hoffman"};

print(legendary_actors >= oscar_winners);

# q
print(avengers_actors - iron_man_actors);

# r
print(dark_knight_actors ^ avengers_actors);

# s
print(iron_man_actors | dark_knight_actors);

# t
fs_legendary_actors: frozenset[str] = frozenset(legendary_actors);
print(fs_legendary_actors);

# Exercise 2
'''
Sets is an unordered collections,
which mean The order of elements can change even if the contents of the set remain the same,
especially after adding or removing element, that is the reason trying to access elements by position is not allowed
'''

# Exercise 3
'''
In a dictionary, keys must be unique, and in a set, all elements must be unique.
This is because both sets and dictionary keys are stored as entries in a hash table,
where each key or element must map to a unique hash.
'''

# Exercise 4
my_set: set[int] = {i for i in range(1, 101)};
print(my_set);

# Exercise 5
import random
my_list: list[int] = [random.randint(1, 10) for i in range(1, 10)];
print(my_list);
print(len(set(my_list)));

