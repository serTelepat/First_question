import random as rand
k = int(input())
list_K = []

for i in range(k):
    number_of_random_for_list_K = rand.randint(-30, 30)
    list_K.append(number_of_random_for_list_K)

print(list_K)
list_K.sort()

print("Sorting: ", list_K)