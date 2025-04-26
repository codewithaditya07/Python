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
print(res)
