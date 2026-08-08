#reverse a list
list1 = [1, 2, 3, 4, 5]
reversed_list = list1[::-1]
print("The reversed list is:", reversed_list)

#reversed list using a loop
list2 = [1, 2, 3, 4, 5]
reversed_list_loop = []
for i in range(len(list2)-1, -1, -1):
    reversed_list_loop.append(list2[i])
print("The reversed list using a loop is:", reversed_list_loop)