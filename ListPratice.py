# Q1 Reverse a list in Python

# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

#Q2 Concatenate two lists index-wise

# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

# Q3 Turn every item of a list into its square

# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in numbers:
#     res.append(i * i)
# print(res)


#Q4 Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]

#Q5 print(res)Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

#Q6 Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)


#Q7 Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Q8 Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

#Q9 Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

# Q10 Remove all occurrences of a specific item from a list.
# list1 = [5, 20, 15, 20, 25, 50, 20]
# def remove_value(sample_list, val):
#     return [i for i in sample_list if i != val]

# res = remove_value(list1, 20)
# print(res)
