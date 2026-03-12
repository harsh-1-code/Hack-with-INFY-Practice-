'''
Problem 1: Maximum Non-Adjacent Same Dish
 
Ramu has N dishes of different types arranged in a row: A1,A2,…,AN where Ai denotes the type of the ith dish. He wants to choose as many dishes as possible from the given list but while sa sfying two conditions:
• He can choose only one type of dish.
• No two chosen dishes should be adjacent to each other.
Ramu wants to know which type of dish he should choose from, so he can pick the maximum number of dishes.
If multiple types give the same maximum count, return the smallest dish type.
Example

Input
N = 9
A = [1,2,2,1,2,1,1,1,1]

Output
1
Explanation:
For type 1 , Ramu can choose at most four dishes. One of the ways to choose four dishes of type 1 is A1,A4, A7 and A9.
For type 2 , Ramu can choose at most two dishes. One way is to choose A3 and A5.
So in this case, Ramu should go for type 1 , in which he can pick more dishes.
So answer = 1.
 

INPUT FORMAT:
• The first line contains T, the number of test cases. Then the test cases follow.
• For each test casem the first line contains a single integer N.
• The second line contains N integers A1, A2, … AN.
 
OUTPUT FORMAT:
For each test case, print a single line containing one integer - the type of the dish that Ramu should choose from. If there are multiple answers, print the smallest one.


'''

T = int(input())
for _ in range (T):
    N = int(input())
    A=list(map(int, input().split()))
    types =set(A)
    best_type=min(types)
    max_count= 0

    for t in types:
        last=-2
        count=0

        for i in range (N):
            if A[i]==t and i-last>1 :
                count+=1
                last=i

            if count >max_count or (count == max_count and t<best_type):
                max_count = count
                best_type =T
    print("best_type",best_type) 

# terminal output 
# harshsingh@Harshs-MacBook-Air Harsh CODE % python -u "/Users/harshsingh/Desktop/Harsh CODE/PYTHON/HWI/problem_1MaximumNonAdjacentSameDish.py"
# 1
# 9
# 1 2 2 1 2 1 1 1 1
# best_type 1
