"""
CTEC 121
Esther
module 6
lab 1 loops
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    for i in range(0, 11, 2):
        print(i)

    count = 0
    while(count < 11):
        print(count)
        #count = count + 2
        count += 2


main()
