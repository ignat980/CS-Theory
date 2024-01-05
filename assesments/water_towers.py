import sys
reverse_enumerate = lambda l: zip(range(len(l) - 1, -1, -1), reversed(l))


def water_trapped(towers):
    max_tower = 0
    total = 0
    look_ahead = []
    # Build array of tower sizes
    # towers=
    #            _
    #      _    | |_   _
    #  _ _| |  _| | |_| |
    # | | | | | | | | | |
    # |_|_|_|_|_|_|_|_|_|
    # *************************
    # look_ahead=
    #            _ _ _ _
    #      _ _ _| | | | |
    #  _ _| | | | | | | |
    # | | | | | | | | | |
    # |_|_|_|_|_|_|_|_|_|
    for tower in towers:
        if tower > max_tower:
            max_tower = tower
        look_ahead.append(max_tower)
    max_tower = 0
    # Calculate difference between max tower and look_ahead in reverse
    #  . . . . . , , , ,
    # : : :,:,:,| |.:.:.:
    # :,:,: |x|x| | |x| |
    # | | | |x| | | | | |
    # |_|_|_|x|_|_|_|_|_|_
    for i, tower in reverse_enumerate(towers):
        if tower >= max_tower:
            max_tower = tower
        else:
            if max_tower > look_ahead[i]:
                if look_ahead[i] > tower:
                    total += look_ahead[i] - tower
            else:
                total += max_tower - tower
    return total

# the code above works likes this:
# 1. find the max tower
# 2. build an array of max towers from left to right
# 3. find the max tower from right to left
# 4. calculate the difference between the max tower and the look_ahead
# 5. if the max tower is greater than the look_ahead, calculate the difference
#    between the max tower and the current tower
# 6. if the look_ahead is greater than the max tower, calculate the difference
#    between the look_ahead and the current tower
# 7. add the difference to the total
# 8. return the total

if __name__ == '__main__':
    towers = sys.argv[1:]
    towers = [int(tower) for tower in towers]
    print(water_trapped(towers))
