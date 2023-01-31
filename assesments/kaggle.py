"""
Exercise: Conditions and Conditional Statements

In the tutorial, you learned about conditions and conditional statements. In this exercise, you will use what you learned to answer several questions.
"""

# from learntools.core import binder
# binder.bind(globals())
# from learntools.intro_to_programming.ex4 import *
# print('Setup complete.')

"""
Question 1

You work at a college admissions office. When inspecting a dataset of college applicants, you notice that some students have represented their grades with letters ("A", "B", "C", "D", "F"), whereas others have represented their grades with a number between 0 and 100.

You realize that for consistency, all of the grades should be formatted in the same way, and you decide to format them all as letters. For the conversion, you decide to assign:

"A" - any grade 90-100, inclusive
"B" - any grade 80-89, inclusive
"C" - any grade 70-79, inclusive
"D" - any grade 60-69, inclusive
"F" - any grade <60
Write a function get_grade() that takes as input:

score - an integer 0-100 corresponding to a numerical grade
It should return a Python string with the letter grade that it corresponds to. For instance,

A score of 85 corresponds to a B grade. In other words, get_grade(85) should return "B".
A score of 49 corresponds to an F grade. In other words, get_grade(49) should return "F".
Make sure that when supplying the grade that is returned by the function, it is enclosed in quotes. (For instance, if you want to return "A", you should write return "A" and not return A.)
"""

# TODO: Edit the function to return the correct grade for different scores
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


"""
Question 2

In the exercise for the previous lesson, you wrote a function cost_of_project() that estimated the price of rings for an online shop that sells rings with custom engravings. This function did not use conditional statements. In this exercise, you will rewrite the function to use conditional statements. Recall that the online shop has the following price structure:

Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
Spaces and punctuation are counted as engraved units.
Your function cost_of_project() takes two arguments:

engraving - a Python string with the text of the engraving
solid_gold - a Boolean that indicates whether the ring is solid gold
It should return the cost of the project.

The function has been partially completed for you, and you need to fill in the blanks to complete the function.
"""

def cost_of_project(engraving, solid_gold):
    if solid_gold:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 * len(engraving)
    return cost


"""

Question 3
You are a programmer at a water agency. Recently, you have been tasked to write a function get_water_bill() that takes as input:

num_gallons = the number of gallons of water that a customer used that month. (This will always be an integer with no decimal part.)
It should output the water bill.

The water agency uses this pricing structure:

Tier	Amount in gallons	Price per 1000 gallons
Tier 1	0 - 8,000	$5
Tier 2	8,001 - 22,000	$6
Tier 3	22,001 - 30,000	$7
Tier 4	30,001+	$10
For example:

Someone who uses 10,000 gallons of water in a month is placed in Tier 2, and needs to pay a water bill of $6 * 10 = $60. In other words, get_water_bill(10000) should return 60.0.
Someone who uses 25,000 gallons of water in a month is placed in Tier 3, and needs to pay a water bill of $7 * 25 = $175. In other words, get_water_bill(25000) should return 175.0.
Do not round your answer. So, your answer might return fractions of a penny.
"""

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        return 5 * num_gallons / 1000
    elif num_gallons <= 22000:
        return 6 * num_gallons / 1000
    elif num_gallons <= 30000:
        return 7 * num_gallons / 1000
    else:
        return 10 * num_gallons / 1000

"""
Question 4

You work for a company that provides data services. For $100/month, your company provides 15 gigabytes (GB) of data. Then, any additional data is billed at $0.10/MB (or $100/GB, since 1,000 MB are in 1 GB).

Use the next code cell to write a function get_phone_bill() that takes as input:

gb = number of GB that the customer used in a month
It should return the customer's total phone bill.

For instance:

A customer who uses 10 GB of data in one month is billed only $100, since the usage stayed under 15 GB. In other words, get_phone_bill(10) should return 100.
A customer who uses 15.1 GB (or 15 GB + 100 MB) of data in one month has gone over by .1 GB, so they must pay $100 (cost of plan), plus $0.10 * 100 = $10, for a total bill of $110. In other words, get_phone_bill(15.1) should return 110.
Do not round your answer.
"""

def get_phone_bill(gb):
    if gb <= 15:
        return 100
    else:
        return 100 + 100 * (gb - 15)


"""
Exercise: Intro to Lists
In the tutorial, you learned how to define and modify Python lists. In this exercise, you will use your new knowledge to solve several problems.
"""

# from learntools.core import binder
# binder.bind(globals())
# from learntools.intro_to_programming.ex5 import *
# print('Setup complete.')

"""
Question 1

You own a restaurant with five food dishes, organized in the Python list menu below. One day, you decide to:

remove bean soup ('bean soup') from the menu, and
add roasted beet salad ('roasted beet salad') to the menu.
Implement this change to the list below. While completing this task,

do not change the line that creates the menu list.
your answer should use .remove() and .append().
"""

# Do not change: Initial menu for your restaurant
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu
menu[1] = 'roasted beet salad'


"""
Question 2

The list num_customers contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days). Fill in values for each of the following:

avg_first_seven - average number of customers who visited in the first seven days
avg_last_seven - average number of customers who visited in the last seven days
max_month - number of customers on the day that got the most customers in the last month
min_month - number of customers on the day that got the least customers in the last month
Answer this question by writing code. For instance, if you have to find the minimum value in a list, use min() instead of scanning for the smallest value and directly filling in a number.
"""

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7]) / 7
avg_last_seven = sum(num_customers[-7:]) / 7
max_month = max(num_customers)
min_month = min(num_customers)

"""
Question 3
In the tutorial, we gave an example of a Python string with information that was better as a list.

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

You can actually use Python to quickly turn this string into a list with `.split()`. In the parentheses, we need to provide the character should be used to mark the end of one list item and the beginning of another, and enclose it in quotation marks. In this case, that character is a comma.

print(flowers.split(","))
['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle']

Now it is your turn to try this out! Create two Python lists:

`letters` should be a Python list where each entry is an uppercase letter of the English alphabet. For instance, the first two entries should be "A" and "B", and the final two entries should be `"Y"` and `"Z"`. Use the string `alphabet` to create this list.
`address` should be a Python list where each row in `address` is a different item in the list. Currently, each row in `address` is separated by a comma.
"""

# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split(".")
formatted_address = address.split(",")


"""
Question 4
In the Python course, you'll learn all about list comprehensions, which allow you to create a list based on the values in another list. In this question, you'll get a brief preview of how they work.

Say we're working with the list below.

test_ratings = [1, 2, 3, 4, 5]

Then we can use this list (`test_ratings`) to create a new list (`test_liked`) where each item has been turned into a boolean, depending on whether or not the item is greater than or equal to four.

test_liked = [i>=4 for i in test_ratings]
print(test_liked)

In this question, you'll use this list comprehension to define a function `percentage_liked()` that takes one argument as input:

* `ratings`: list of ratings that people gave to a movie, where each rating is a number between 1-5, inclusive

We say someone liked the movie, if they gave a rating of either 4 or 5. Your function should return the percentage of people who liked the movie.

For instance, if we supply a value of `[1, 2, 3, 4, 5, 4, 5, 1]`, then 50% (4/8) of the people liked the movie, and the function should return `0.5`.

Part of the function has already been completed for you. You need only use `list_liked` to calculate `percentage_liked`.

"""

def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = len(list_liked) / len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])