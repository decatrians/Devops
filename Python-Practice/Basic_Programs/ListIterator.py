list1=list(input("Enter list objects:").split())
print(list1)
print(list(set(list1)))
duplicate = []
unique = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j] and list1[i] not in duplicate :
            duplicate.append(list1[i])
            break
    if list1[i] not in duplicate and list[i] not in unique:
            unique.append(list1[i])


print(duplicate)
print(unique)