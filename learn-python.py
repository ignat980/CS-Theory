def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

# O(nm(log(n)+log(m)))
def permutation(str, prefix=""):
    if len(str) == 0:
        print(prefix)
    else:
        for i in range(len(str)):
            rem = str[0:i] + str[i+1:]
            permutation(rem, prefix + str[i])

# O(2^n)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# O(n)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# O(n), arr must be sorted
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid+1, r, x)
    else:
        return -1    

if __name__ == "__main__":
    # n = int(input("Enter a number: "))
    # print(sum(n))
    # s = input("Enter a string: ")
    # permutation(s)
    # n = int(input("Enter a number: "))
    # print(fib(n))
    # n = int(input("Enter a number: "))
    # print(factorial(n))
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index %d" % result)
    else:
        print("Element is not present in array")