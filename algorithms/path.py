def does_path_exist(d, key1, key2, visited=set()):
    # Is the node adjecent to the current node
    if key2 in d[key1]:
        return True
    # Have we visited the node before
    if key1 in visited:
        return
    # For every adjecent node, see if there is a path to key2
    for key in d[key1]:
        # Keep track of visited nodes
        visited.add(key)
        # If a path exists, return true
        if does_path_exist(d, key, key2, visited):
            return True
    # After you visit every adjecent node, and a path is not found, return False
    return False
