#  Selection sort

a = [23,12,34,23,1,2,3,4,63,35,65,32,123,45]

for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_index]:
            min_index = j
    a[i] , a[min_index] = a[min_index],a[i]

a
