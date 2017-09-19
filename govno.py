a = []
print ("PLease, enter the array of numbers\n")
for i in range (10):
    a.append(input())
for i in range (10):
    for j in range (10):
        if a[i]<a[j]:
            b = a[i]
            a[i] = a[j]
            a[j] = b
for i in range(10):
    print (a[i])

