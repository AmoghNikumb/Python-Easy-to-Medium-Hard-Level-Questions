List1 = [1, 2, 3, 1, 1, 4, 5, 2, 4, 5, 3, 3, 3]
max_count = List1.count(List1[0])
print(max_count)
element = List1[0]

for cnt in List1:
    if element != cnt:
        if List1.count(cnt) > max_count:
            max_count = List1.count(cnt)
            element = cnt

print(element, 'has occured', max_count, 'times')
