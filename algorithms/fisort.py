def fisort(array):
    if not array:
        return []
    end = start = array[0]
    sort = [start]
    for val in array[1:]:
        print(sort, start, end, val)
        if val < start or val == start:
            sort.insert(0, val)
            start = val
            continue
        elif val > end or val == end:
            sort.append(val)
            end = val
            continue
        else:
            num = len(sort) * (val - start) / (end - start)
            print(num)
            idx = int(num)
            print("pre idx:", idx)
            if val < sort[idx]:
                while val < sort[idx - 1]:
                    idx -= 1
                print("< idx:", idx)
                sort.insert(idx, val)
            elif val > sort[idx]:
                while val > sort[idx + 1]:
                    idx += 1
                print("> idx:", idx)
                sort.insert(idx + 1, val)
            else:
                sort.insert(idx, val)
    return sort
