# Project Euler - Problem 0 (Account Creation)
#
# A square number is the square of a positive integer.
# The first 5 square numbers are: 1, 4, 9, 16, 25
# Among those, the odd squares are: 1, 9, 25 -> sum = 35
#
# Question: Among the first 463,000 square numbers,
# what is the sum of all the odd squares?


def solve():
    first = 463000
    running_sum = 0
    for i in range(1,first, 2):
        # print("i = " + str(i))
        running_sum += i**2
    return running_sum

if __name__ == '__main__':
    print(solve())
