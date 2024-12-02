# SET

s1 = {1,1,2,3,"Ravi"}
print(s1)  # Duplicates are removed

# Convert list to set
L1 = [3,4,5,6,6,"Ravi","Geetha",45]
s2 = set(L1)
print(s2)

# union all
s3 = {3,4,5,6}
s4 = {4,5,6,7,8}
s5 = s3.union(s4)
print(s5)

# Intersection

s6 = {1,2,3,4,5}
s7 = {4,5,6,7,8}
s8 = s6.intersection(s7)
print(s8)

# Difference

s9 = {2,3,4,5}
s10 = {4,5,6,7}
s11 = s9.difference(s10) # o/p - will be 1st set
print(s11)
# s11 = s10.difference(s9)
# print(s10)
