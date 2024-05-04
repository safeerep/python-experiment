# set
Set = set([1, 2, 'safee', 4, 'mon', 7, 'ep']) 
print("\n Set with the use of Mixed Values") 
Set.add("masterpadi")
print(Set) 

print("safeer" in Set) # it will print false
print("safee" in Set) # it will print true

# frozen set
Set2 = frozenset([1, 2, 'safee', 4, 'mon', 7, 'ep'])
print("frozen set is \n")
print( Set2)
# we can't add to frozen set
# Set2.add