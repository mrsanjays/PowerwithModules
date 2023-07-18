def PowerwithModules(A,B,C):
    res=1
    for _ in range(B):
        A%=C
        res=(res*A)%C
    return res
if __name__ == '__main__':
    A,B,C=map(int,input().split())
    print(PowerwithModules(A,B,C))

"""

 You are given A, B and C .
 Calculate the value of (A ^ B) % C

 Example Input

 Input 1:
 A = 2 B = 3 C = 3
 Input 2:
 A = 5 B = 2 C = 4


 Example Output

 Output 1: 2
 Output 2: 1

 """