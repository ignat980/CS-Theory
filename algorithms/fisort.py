def insertion_sort(array):
    """A bit faster insertion sort

    This variation decides where the index should be before inserting.
    Ω(n), O(n^2)
    """
    if not array:
        return []
    end = start = array[0]
    sort = [start]  # The returned array; TODO optimize to be in-place
    for val in array[1:]:
        print(sort, start, end, val)  # Debug
        # insert at beginning if < min
        if val < start or val == start:
            sort.insert(0, val)
            start = val
        # insert at end if > max
        elif val > end or val == end:
            sort.append(val)
            end = val
        else:
            # Figure out what the index should be
            num = len(sort) * (val - start) / (end - start)
            print(num)
            idx = int(num)
            print("pre idx:", idx)  # Debug
            # Insertion sort from the index
            if val < sort[idx]:
                while val < sort[idx - 1]:
                    idx -= 1
                print("< idx:", idx)  # Debug
                # O(N) time to insert :(
                sort.insert(idx, val)
            elif val > sort[idx]:
                while val > sort[idx + 1]:
                    idx += 1
                print("> idx:", idx)  # Debug
                sort.insert(idx + 1, val)
            else:
                sort.insert(idx, val)
    return sort
