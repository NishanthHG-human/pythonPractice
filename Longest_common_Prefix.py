

strs = ["flower","flow","flight"]
my_dict= {index: value for index,value in enumerate(strs)}
print(my_dict)

for i in range(len(my_dict[0])):
    if my_dict[0][i] == my_dict[1][i] == my_dict[2][i]:
        print("Its working")
    else:
        print()



# def longestcommonprefix(strs1):
#     list1 = strs1[0]
#     list2 = strs1[1]
#     list3 = strs1[2]
#
#     for i in range(len(strs1)):
#         if list1[i] == list2[i] == list3[i]:
#             return list1[i]
#         else:
#             break

    # if count > 0:
    #     my_list = []
    #     for i in range(count):
    #         my_list.append(list1[i])
    #     print(str(my_list))
    # else:
    #      print("")


# print(longestcommonprefix(strs))
