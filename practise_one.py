# hello comments
_variable = "String"
# True = 1 , reserved words


def myFunc(a, b=5):
    return a + b


a = myFunc(1)

# or  -> returns first truthy value, if no truthy value then last falsy value
# and -> returns first falsy value, if no falsy value then last truthy value
b = 0 or False or 1 or None
c = 1 and True and ""

# check boolean equivalent of a value
d = bool("")
# print(d)

# list
l1 = ["a", "b", "c", "d"]
# access by index
l1[1]
# range
print(l1[1:3], l1[:5], l1[2:], l1[:-1])
# length
print("length of list = ", len(l1))
# list methods
l1.append("e")
# copy by reference
l2 = l1
# normal copy
l3 = l1.copy()
l1.append(2)
print("after append ", l1)
print("l2 ", l2)
print("l3 ", l3)

l1.append(2)
l1.append(2)
# count number of value
two_count_in_l1 = l1.count(2)
print(two_count_in_l1)
print("hello world universe hello".count("hello"))
