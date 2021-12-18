import numpy as np

# rows and columns
X=[]
n,p=[int(x) for x in input().split()]
for _ in range(n):
    x=[float(x) for x in input().split()]
    X.append(x)

X=np.array(X).reshape(n,p)

print(X)
ave=np.mean(X,axis=1)
res=[]
for i in range(n):
    res.append(round(ave[i],2))
print(np.array(res))



""" Problem
Data Science - Average of Rows


In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]
Explanation
The first row has two numbers 1.5 and 1, thus the sum is 1.5 + 1 = 2.5 and the mean is then 2.5/2 = 1.25. Then for the second row, the average is calculated as (2 + 2.9)/2 = 4.9/2 = 2.45.
"""

