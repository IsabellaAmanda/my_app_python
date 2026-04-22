### Tuples ###
#los valores son inmutables, son constantes, no cambian
my_tuple = tuple()
my_other_tuple = (60, 30)

my_tuple = (20, 1.61, "Isabella", "Cordero", "Isabella")
print(my_tuple)

print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Isabella"))
print(my_tuple.index("Cordero"))
print(my_tuple.index("Isabella"))

#my_tuple[1] = 1.80 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_lits_tuple = list(my_tuple)
print(type(my_lits_tuple))

my_lits_tuple[4] = "ChavellaCod"
my_lits_tuple.insert(1, "Gold")
my_tuple = tuple(my_lits_tuple)
print(tuple(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion
#print(my_tuple) NameError: name 'my_tuple' is not defined




