"""
#印圖形

請使用 while loop或for loop，
請使用 function。
Input
-------
n=1
output
--------
#1
--------
Input
-------
n=2
output
--------
##21
###1
------------
Input
-------
n=3
output
--------
###321
####21
#####1
----------
Input
-------
n=4
output
--------
####4321
#####321
######21
#######1
----------
Input
-------
n=5
output
--------
#####54321
######4321
#######321
########21
#########1
"""
def print01(n):
    for i in range(n):
        print('#',end='')
        
def print02(n):
    for i in range(n,0,-1):
        print(i,end='')
    print("")
def print03(n):
    for i in range (n,2*n,1):
        print01(i)
        print02(2*n-i)
        
def main():
    a=int(input())
    print03(a)
    
main()