def factorial(n):
    '''factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n'''
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    ...
    # return factorial_iterative(n)
    return factorial_recursive(n)


def factorial_iterative(n):
    # implement the factorial function iteratively here
    ...
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests below


def factorial_recursive(n):
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)

def fibonacci(n):
    '''fibonacci(n) returns the n-th number in the Fibonacci sequence,
    which is defined with the recurrence relation:
    fibonacci(0) = 1
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n – 1) + fibonacci(n – 2), for n > 1'''
    # implement fibonacci_iterative and fibonacci_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return fibonacci_iterative(n)
    return fibonacci_recursive(n)


def fibonacci_iterative(n):
    # implement the fibonacci function iteratively here
    ...
    # once implemented, change fibonacci (above) to call fibonacci_iterative
    # to verify that your iterative implementation passes all tests below


def fibonacci_recursive(n):
    # implement the fibonacci function recursively here
    ...
    # once implemented, change fibonacci (above) to call fibonacci_recursive
    # to verify that your recursive implementation passes all tests below


def linear_search(array, item):
    '''return the first index of item in array or None if item is not found'''
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    ...
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    ...
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    '''return the index of item in sorted array or None if item is not found'''
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    ...
    # return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)
    return binary_search_from_class(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    ...
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # implement binary search recursively here
    ...
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search_from_class(array, item):
    '''Kevin's description of binary search:
    1. start in the middle of array
    2. check if item is the middle value
        return middle index
    3. if not, check if item is less than the middle value
        binary search the lower half of array (values left of the middle)
    4. if not, check if item is greater than the middle value
        binary search the upper half of array (values right of the middle)'''
    # check if array is empty
    if len(array) == 0:
        return None
    # middle index is half the array length
    middle = len(array) // 2
    # check if item is the middle value of array
    if item == array[middle]:
        return middle
    # check if item is less than the middle value of array
    elif item < array[middle]:
        # search left half of array recursively
        left_half = array[0: middle]
        result = binary_search(left_half, item)
        # ensure None is propogated upwards if item was not found recursively
        return None if result is None else result
    # check if item is greater than the middle value of array
    elif item > array[middle]:
        # search right half of array recursively
        right_half = array[middle + 1: len(array)]
        result = binary_search(right_half, item)
        # ensure None is propogated upwards if item was not found recursively,
        # otherwise adjust the returned index due to slicing the array in half
        return None if result is None else result + middle + 1
