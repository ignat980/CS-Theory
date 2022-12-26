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


if __name__ == '__main__':
    towers = sys.argv[1:]
    towers = [int(tower) for tower in towers]
    print(water_trapped(towers))
