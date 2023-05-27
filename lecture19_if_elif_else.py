"""
If X is divisible by 2
    Then you will state "X is even"
Otherwise
    Then you will state "X is odd"
"""

x = 6

if x%2==0: 
    print("X is even")
if x%2!=0: 
    print("X is odd")

"""
Left == Right -> True if the Left value and the Right value will be same
Left == Right -> False if the Left value and the Right value will be different
"""

## Homework:
"""
marks = Take the input and assume that the marks can be integer only
0 <= marks <= 100

marks >=90 print("Grade A")
marks >= 75 and marks < 90 then print("Grade B")
marks >= 60 and marks <75 then print("Grade C")
marks < 60 then print("FAIL")
"""

marks = int(input("Enter Your Marks: "))
if marks>=90:
    print("Grade A")
elif marks>=75 and marks<90:
    print("Grade B")
elif marks>=60 and marks<75:
    print("Grade C")
else:
    print("FAIL")
