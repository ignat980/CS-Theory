"""Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory, you had to develop a system to track them, since some habitually continue to gnaw on the heads of their brethren and need extra supervision. For obvious reasons, you based your rabbit survivor tracking system on a binary search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age. For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added, older ages to the left and younger to the right. The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation, and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean are contained properly. Since the tree did not preserve the order of rescue, it falls to you to figure out how many different sequences of rabbits could have produced an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result in a binary tree identical to one created from [5, 2, 9, 1, 8].

You must write a function answer(seq) that takes an array of up to 50 integers and returns a string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"
"""
from math import factorial


class BinarySearchTree(object):
    """A Binary Search tree"""
    def __init__(self, *values):

        self.root = None
        self.left = None
        self.right = None

        for value in values:
            self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = value
        elif value < self.root:
            if isinstance(self.left, BinarySearchTree):
                self.left.insert(value)
                print(self.left)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.root:
            if isinstance(self.right, BinarySearchTree):
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            raise ValueError('Values are expected to be unique')

    def __repr__(self):
        return "BST(Root:" + repr(self.root) + ", Left:" + repr(self.left) + ", Right:" + repr(self.right) + ")"


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def count(tree):
    total = 0
    if isinstance(tree, BinarySearchTree):
        total += 1 + count(tree.left) + count(tree.right)
    return total


def permutations(tree):
    if not tree:
        return 1

    leftCount = count(tree.left)
    rightCount = count(tree.right)

    leftPermutations = permutations(tree.left)
    rightPermutations = permutations(tree.right)

    return choose(leftCount + rightCount, rightCount) * leftPermutations * rightPermutations


def answer(*bunnyList):
    return permutations(BinarySearchTree(*bunnyList))


if __name__ == '__main__':
    temp = [5, 8, 9, 3, 1, 4]
    print("List:", temp)
    print("Possible permutations:", answer(*temp))
