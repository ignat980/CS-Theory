# Hello world!

# you have to buy N bottles of soda, but the store sells soda in spcific packs, like in packs of 1, 6, 12, or 20.
# return all the possible combinations of packs to buy N sodas.
# Example:
# N = 7, [2, 3, 5, 12, 20]
# [[2, 2, 3], [2, 3, 2], [3, 2, 2]]

# 7, []
# 5, [2]
# 3, [2, 2]
# 1, [2, 2, 2]
# 3, [2, 2]
# 0, [2, 2, 3]


def soda(N, packs):
    returned = []
    for pack in packs:
        print("Pack:", pack)
        ways = []
        if N - pack >= 0:
            for way in [[pack]] + soda(N - pack, packs):
                print("Way:", way)
                ways.append(way)
            if ways:
                returned.append(ways)
        else:
            break
    return returned

# def soda(N, packs):
#     returned = []
#     bottles = N  # 7
#     steps = []
#     pack_index = 0
#     for pack in packs:
#         while bottles > 0:
#             steps.append(packs[pack_index])  # [1]
#             bottles -= packs[pack_index]  # 6
#             # [1, 1, 1, 1, 1, 1, 1]; N = 0
#             # bottles += steps.pop()
#             # [1, 1, 1, 1, 1, 1]; N = 1
#         while bottles < 0:
#             if bottles < 0:
#                 bottles += steps.pop()
#                 bottles += steps.pop()
#                 pack_index += 1
#                 steps.append(packs[pack_index])
#                 bottles -= packs[pack_index]
#             elif bottles == 0:
#                 returned.append(steps)
#                 bottles += steps.pop()
#                 bottles += steps.pop()
#         if bottles - pack >= 0:  # 1 - 6 !>= 0
#             # Doesn't get run
#             steps.append(packs[pack_index])  # [1, 1, 1, 1, 1, 1, 6]
#             bottles -= packs[pack_index]  # N = -5
#         else:
#             break  # breaks
#     # [1, 1, 1, 1, 1, 1]; N = 1
#     bottles += steps.pop()
#     # [1, 1, 1, 1, 1]; N = 2
#     pack_index += 1
#     steps.append(packs[pack_index])
#     bottles -= packs[pack_index]
#     # [1, 1, 1, 1, 1, 6]; N = -4

#     return returned
#
# i have a total
# I keep subtracting the current pack until the total is 0, keep track of the steps
# I add the steps to get to 0 to the returned array, which is one combination
# I undo one step and then subteract the next pack and check if it is less then
# if it is, go back one step, other wise append the steps

# 7 - 6

#
