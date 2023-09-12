# 1. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# size = int(input("Enter the size of the list: "))
# lst = []

# for i in range(size):
#     values = input("Enter the value separated by a comma ',': ")
#     tup_val = tuple(map(int, values.split(',')))
#     lst.append(tup_val)

# sorted_lst = []

# while lst:
#     min_val = lst[0]
#     for j in lst:
#         if j[-1] < min_val[-1]:
#             min_val = j
#     sorted_lst.append(min_val)
#     lst.remove(min_val)
# print("Sorted list: ",sorted_lst)


 # 2. Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

alph_dict = {}
alph = [chr(ord('a')+i) for i in range(26)]
asc_val = [ord(char) for char in alph]
for i in range(26):  
    alph_dict[alph[i]] = asc_val[i]
print("Your Dictionary: ",alph_dict)