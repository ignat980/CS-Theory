"""
Name that rabbit
================

"You forgot to give Professor Boolean's favorite rabbit specimen a name?
You know how picky the professor is! Only particular names will do!
Fix this immediately, before you're... eliminated!"

Luckily, your minion friend has already come up with a list of possible names,
and we all know that the professor has always had a thing for names
with lots of letters near the 'tail end' of the alphabet, so to speak.
You realize that if you assign the value 1 to the letter A, 2 to B,
and so on up to 26 for Z, and add up the values for all of the letters,
the names with the highest total values will be the professor's favorites.
For example, the name Annie has value 1 + 14 + 14 + 9 + 5 = 43, while the name Earz,
though shorter, has value 5 + 1 + 18 + 26 = 50.

If two names have the same value, Professor Boolean prefers the lexicographically larger name.
For example, if the names were AL (value 13) and CJ (value 13), he prefers CJ.

Write a function answer(names) which takes a list of names and
returns the list sorted in descending order of how much the professor likes them.

There will be at least 1 and no more than 1000 names.
Each name will consist only of lower case letters.
The length of each name will be at least 1 and no more than 8.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) names = ["annie", "bonnie", "liz"]
Output:
    (string list) ["bonnie", "liz", "annie"]

Inputs:
    (string list) names = ["abcdefg", "vi"]
Output:
    (string list) ["vi", "abcdefg"]

Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.
"""


def answer(names):
    # Sort to have CJ before AL (decending order)
    names = sorted(names, reverse=True)
    # Creates a tuple of (name, sum) for each name then puts it in a list
    nametotal_pairs = [(name, sum([ord(letter) - 96 for letter in name])) for name in names]
    # Sorts a list based on the sum in decending order, then strips the sum
    return [name[0] for name in sorted(nametotal_pairs, key=lambda total: total[1], reverse=True)]

if __name__ == '__main__':
    print(answer(["annie", "bonnie", "liz"]))
    print(answer(["abcdefg", "vi"]))
    print(answer(["AL", "CJ"]))
