for i in range(5):
	print(i)

sum = 0
for i in range(10):
	sum = sum +i
print(sum)

for k in (1,2,3):
	print(k)
else:
	print('Done')

list1 = list(range(2, 5))
print(list1)
list2=list(range(4, 1, -1))
print(list2)
list3=list(range(2, -3, -1))
print(list3)

s='How are you'
lst = [s, (1, 2, 3), {'abc', 'xyz'}]
for i1 in range(len(lst)):
    print(lst[i1])

print(['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]])
 
