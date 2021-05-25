# from numpy import mean


# number_list = [45, 34, 10, 36, 12, 6, 80]
# avg = mean(number_list)
# print("The average is ", round(avg, 2))


def avg(mylist):
    return sum(mylist) / len(mylist)


L = [1, 5, 2, 8, 9, 3, 4, 0]
print(avg(L))
