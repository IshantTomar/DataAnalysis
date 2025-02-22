# # ----- Q1. Remove extra spaces in all strings in a list.
#
# def fillteredList(a):
#     fixedList = []
#     for x in a:
#         fixedList.append(" ".join(x.split()))
#     return fixedList
#
# li = [" Hi ", " A setence   with extra     spaces ", " Another  sentence"]
#
# print(fillteredList(li))
#
#
# # ----- Q2. Reverse all strings in a list.
#
# def reverseListFunction(a):
#     reversedList = []
#     for x in a:
#         reversedList.append(x[::-1])
#     return reversedList
#
# li = ["one", "two", "three", "four", "five"]
# print(reverseListFunction(li))
#
#
# # ----- Q3. Filter all strings with K in a list. K is given from user.
#
# def startsWithUserInput(userInput, passedList):
#     filltereddList = []
#     for x in passedList:
#         if x.lower().startswith(userInput.lower()):
#             filltereddList.append(x)
#     return filltereddList
#
# li = ["Hi means hello", "two is 2", "five is 5", "Another string", "Hello"]
# user = input("Enter: ")
#
# print(startsWithUserInput(user, li))
#
#
# # ----- Q4. Union of two or more list.
#
# def unionList(passedList1, passedList2, passedList3):
#     newList = list(set(passedList1 + passedList2 + passedList3))
#     return newList
#
# li1 = [2,4,6]
# li2 = [2,3,5,4,7]
# li3 = ["a",2,"c"]
#
# print(unionList(li1,li2,li3))
#
#
# # ----- Q5. Find all the combination in the list satisfying some condition.
#
# def combinationList(passedList, passedCondition):
#     filteredList = []
#     for i in passedList:
#         if passedCondition(i):
#             filteredList.append(i)
#     return filteredList
#
# li = [1,2,3,4,5,6,7,8,9,10,11]
# condition = lambda x: x % 2 != 0
#
# print(combinationList(li, condition))
#
# # ------------ 2nd way -----------------
#
# li = [1,2,3,4,5,6,7,8,9,10,11]
# condition = lambda x: x % 2 != 0
#
# combinationList = list(filter(condition, li))
#
# print(combinationList)