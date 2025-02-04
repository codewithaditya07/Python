# lst = ['rohan', 'shyam','rohit','shree','happy']
# d=dict.fromkeys(lst,100)
# print(len(lst))
# print(d)

#merge dictionary
# d1 = {'apple': 1,'mango': 2}
# d2 = {'banana': 3,'kiwi':4}
# d3 = {'watermelon':5,'gauva':6}
# d4 = (d1,d2,d3)
# d5 = {}
# for i in d4:
#     d5.update(d4)
# print(d4)


    # write a program to check dictionary is empty or not
# d1 = {'app': 1,'man': 2}
# d2 = {'ban': 3,'kiwi':4}
# d3 = {'water':5,'gauva':6}
# d4 = {}
# tpl = (d1,d2,d3,d4)
# for i in tpl:
#     if(i):
#      print("true")
#     else:
#      print("false")


# d1 = {'apple': 1,'mango': 2}
# d2 = {'water':5,'gauva':6}
# d3 = {**d1,**d2}
# print(d3)

# d = {
#    'anuj':{'salary': 10000,'age':20,},
#    'anshul':{'salary': 15000,'age':25,},
#    'parth':{'salary': 33000,'age':26,}
# }
# lst = []

# for i in d.values():
#      lst.append(i['salary'])

# print( "max",max(lst))
# print( "min",min(lst))


lst = [1,2,2,3,3,3,4,4,4,4]
freq = {}
for i in lst:
    freq[i] = freq.get(i , 0)+1
    
print(freq)

