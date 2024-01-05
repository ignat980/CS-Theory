"""Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits!
But instead of following the Fibonacci sequence like all good rabbits do,
the zombit population changes according to this bizarre formula,
where R(n) is the number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(3) = R(2*1 + 1) = R(1 - 1) + R(1) + 1 = 3
R(4) = R(2*2) = R(2) + R(2*1 + 1) + 2 = 2 + (R(1 - 1) + R(1) + 1) + 2 = 2 + 3 + 2 = 7
R(5) = R(2*2 + 1)

R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program
with only one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman,
a bunch of Professor Boolean's minions passed the time by playing
a guessing game: when will the zombit population be equal to a certain amount?
Then, some clever minion objected that this was too easy,
and proposed a slightly different game: when is the last time that the zombit
population will be equal to a certain amount? And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation,
and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10
string representation of an integer S, returns the largest n such that
R(n) = S. Return the answer as a string in base-10 representation.
If there is no such n, return "None". S will be a positive integer no greater than 10^25.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"
"""
cache = {}


def R(num):
    if num == 0 or num == 1:
        return 1
    if num == 2:
        return 2

    if num not in cache:
        # divide num by two and drop remainder
        halfNum = int(num / 2)
        if num & 1:
            # odd = R(2n+1)
            cache[num] = R(halfNum) + R(halfNum - 1) + 1
        else:
            # even = R(2n)
            cache[num] = R(halfNum) + R(halfNum + 1) + halfNum
    # print("R(", num, ")", " = ", cache[num], sep="")
    return cache[num]


def search(a, b, target, is_odd):
    """
    Does a binary search for the target between a and b, and either odds or evens
    """
    # print
    # print "Search:", a, b
    if b <= a:
        # max less than or equal to min - target not found
        return None
    midpoint = a + int((b - a) / 2)
    # print "Midpoint:", midpoint
    # if midpoint is not odd and is_odd is set, then make midpoint odd
    # if midpoint is odd and is_odd not set, then make midpoint even
    # Basically maintain search in even-space or odd-space
    if is_odd != int(midpoint) & 1:
        midpoint += 1

    # print "Adjusted Midpoint:", midpoint
    S = R(midpoint)
    # print "R(midpoint) =", S
    if S == target:
        return midpoint
    elif S > target:
        # endpoint is now the midpoint
        b = midpoint - 1
    else:
        # startpoint is now the midpoint
        a = midpoint + 1

    # keep searching but with adjusted indices
    return search(a, b, target, is_odd)


def answer(str_S):
    s = int(str_S)
    # search odd first, then even
    return search(0, s, s, 1) or search(0, s, s, 0)

if __name__ == '__main__':
    print "Answer:", answer(str(pow(10, 25)))
    # previous = 1
    # currentEven = 1
    # for i in range(10000000, 10000010):
    #     if i % 2 == 0:
    #         currentEven = R(i)
    #         print(currentEven, previous)
    #         print(currentEven / previous)
    #     previous = R(i) if i != 0 else 1
