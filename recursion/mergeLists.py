##Recursive Merge of two sorted lists

def merge(list1, list2):
    if list1 == []:
        return list2
    elif list2 == []:
        return list1
    else:
        if list1[0] < list2[0]:
            return [list1[0]] + merge(list1[1 :], list2)
        else:
            return [list2[0]] + merge(list1, list2[1 :])


print(merge([2, 4, 5], [3,6]))
