set1={2,3,5,6,8,4,5,7}
set2={2,3,5,9,11,15}
print("set1=",set1)
print("set2=",set2)
#created new set3
set3=set(set1.union(set2))
print(f"{set1}U{set2}={set3}")

#modefied current set1
set1.update(set2)
print(f"{set1}U{set2}={set1}")