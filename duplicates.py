##########################################
# DESCRIPTION:
# Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
# drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
# which leads to [1,2,3,1,2,3].
#
# Example:
# delete_nth ([20,37,20,21],1) # return [20,37,21]
##########################################

import collections


def delete_nth(list, n):
    duples_count = collections.Counter()

    for value in list:
        duples_count[value] += 1

    duples_list = [key for key in duples_count.keys() if duples_count[key] > 1]

    reverse_list = list[::-1]

    for key in duples_list:
        for i in range(duples_count[key] - n):
            reverse_list.remove(key)

    list = reverse_list[::-1]

    print("Final list: ", list)


if __name__ == "__main__":
    delete_nth([20, 37, 20, 21, 37, 1, 20], 2)
