### sets ###
my_sets = set()
my_other_set = {"Isabella", "Cordero", 20}
print(type(my_sets))
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("Maria")
print(my_other_set) #un set no es una estructura ordenada

my_other_set.add("Maria")
print(my_other_set) #un set no admite repetidos

print("Maria" in my_other_set)
print("Marie" in my_other_set)

my_other_set.remove("Maria")
print(my_other_set)


my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) #NameError: name 'my_other_set' is not defined

my_sets = {"Isabella", "Cordero", 20}
my_list = list(my_sets)
print(my_list[0])

my_other_set = {"C", "Python", "Html"}

my_new_set = my_sets.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_sets).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_sets))
