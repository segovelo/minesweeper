from minesweeper import Sentence

s1 = set([1,2,3,4,5,6])
s2 = set([5,6,7,8,9])
s3 = set([1,2])
s4 = set([(1,5),(2,5)])
s5 = set([(2,5), (1,5)])
sentence4 = Sentence(s4, 1)
sentence5 = Sentence(s5, 1)
print(f"{s1} intersection {s2} = {s1.intersection(s2)}")
print(f"{s1} difference {s2} = {s1.difference(s2)}")
print(f"{s2} difference {s1} = {s2.difference(s1)}")
s1.difference_update(s2)
print(f"{s1} difference_update {s2} = {s1}")
print(f"s1 = {s1} After difference_update")
print(f"{s1} is superset {s3} ?  {s1.issuperset(s3)}")
print(f"{s3} is subset {s1} ?  {s3.issubset(s1)}")
s1 = set([1,2,3,4,5,6])
print(f"{s1} update {s2} = {s1.update(s2)}")
print(f"s1 : {s1}")

l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4]
l3 = []

print(f"List_1 : {l1} Union List_2 : {l2}  ->  ")
l2.extend([item for item in l1 if item not in l2])
print(l2)

if s4 == s5:
    print(f"s4: {s4} is equal to s5: {s5}")
else:
    print(f"s4: {s4} is NOT equal to s5: {s5}")

if sentence4.__eq__(sentence5):
    print(f"Sentence4: {sentence4}  is equal to sentence5: {sentence5}")
else:
    print(f"Sentence4: {sentence4}  is NOT equal to sentence5: {sentence5}")