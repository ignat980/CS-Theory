#CS Theory Assessment • 3/30/16

##Conceptual Challenges

####Alternative Resizable Array
When appending an item to the end of a resizable array, there may not be space at the end of the underlying fixed-size array. Creating a new underlying array and copying all the items is a time-consuming operation. What alternative approaches could you use to create a resizable array and how would you implement it?


####Implement a Queue
Assume you have good working implementations of these core list data structures:

* resizable array – operations: `get`, `set`, `size`
* circular buffer – operations: `get`, `set`, `size`
* singly linked list – operations: `head`, `tail`, `append`, `prepend`, `size`

Which are good choices to implement a queue? Explain why or why not for each.

What is time complexity of the `enqueue`, `dequeue`, `front`, and `size` operations?


####Hash Table Buckets
When storing an entry in a hash table, we calculate the key's hash value. Sometimes there is a collision and a new entry hashes to the same bucket as an existing entry. To resolve this with chaining, we use a linked list in each bucket to hold multiple entries. Could we instead use another type of list, like an array or even another hash table? Would that type of list be an improvement over using a linked list? Why or why not?


##Programming Challenges

####Fix the Stack
Your friend's dish-washing robot stacked the plates incorrectly and the first two items were always placed in the wrong order. :-( To help your friend fix this egregious robot error, write a function that takes a stack as input and swaps the bottom two items only.


####Make Change
You're tasked with writing a function for a cash register that shows a teller how to make change for a customer after a transaction. Given a list of coin denominations available and an amount of money, return a list of what coins to give as change.

Example: `change(coins=[1, 5, 10, 25], amount=42)` should return `[25, 10, 5, 1, 1]`

Can you implement this recursively? Does it make it easier to write, or shorter code?

#####Stretch goal: Find all possible combinations of coins to make change and return the one that requires giving the fewest number of coins.


####Find a Pair
Given a list of numbers and a target sum, find a pair of numbers in the list that add to the target sum. What is the time complexity of your solution? How can you improve it?

Example: `find_pair(numbers=[1, 5, 4, 1, 7, -2], target=3)` should return `(5, -2)`

#####Stretch goal: Find all pairs of numbers that add to the target sum, return a list of pairs.
Example: `find_pair(numbers=[3, 5, 7, 2, 0, -2], target=3)` should return `[(5, -2)]`
