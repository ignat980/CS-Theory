"""
Zombit antidote
===============

Forget flu season. Zombie rabbits have broken loose and are terrorizing Silicon Valley residents!
Luckily, you've managed to steal a zombie antidote and set up a makeshift rabbit rescue station.
Anyone who catches a zombie rabbit can schedule a meeting at your station to have it injected with the antidote,
turning it back from a zombit to a fluffy bunny.
Unfortunately, you have a limited amount of time each day,
so you need to maximize these meetings.
Every morning, you get a list of requested injection meetings,
and you have to decide which to attend fully. If you go to an injection meeting,
you will join it exactly at the start of the meeting, and only leave exactly at the end.

Can you optimize your meeting schedule? The world needs your help!

Write a method called answer(meetings) which, given a list of meeting requests,
returns the maximum number of non-overlapping meetings that can be scheduled.
If the start time of one meeting is the same as the end time of another,
they are not considered overlapping.

Meetings will be a list of lists.
Each element of the meetings list will be a two element list denoting a meeting request.
The first element of that list will be the start time and the second element will be
the end time of that meeting request.

All the start and end times will be non-negative integers, no larger than 1000000.
The start time of a meeting will always be less than the end time.

The number of meetings will be at least 1 and will be no larger than 100.
The list of meetings will not necessarily be ordered in any particular fashion.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
Output:
    (int) 4

Inputs:
    (int) meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
Output:
    (int) 1

Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.
"""


def answers(meetings):
    # Sort by the start time
    sorted_meetings = sorted(meetings, key=lambda x: x)
    possible_meetings_count = 0

    # iterate over the sorted meeting list
    for idx, meeting in enumerate(sorted_meetings):
        # There will be at least 1 meeting that you can do
        probable_meetings_count = 1
        # Set the end time to be the end of the current meeting
        end_time = meeting[1]

        # For each next possible meeting in the list
        for next_meeting in sorted_meetings[idx + 1:]:
            # if the start time is less than the end time, look at the next meeting
            if next_meeting[0] < end_time:
                continue

            probable_meetings_count += 1
            # End time is now end of the next meeting
            end_time = next_meeting[1]

        possible_meetings_count = max(probable_meetings_count, possible_meetings_count)
    return possible_meetings_count

if __name__ == '__main__':
    print(answers([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]))
    print(answers([[0, 1], [1, 500], [2, 500], [3, 500], [4, 500]]))
