import math
def ncr(self,n,r):
        return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
def generate(self, numRows: int) -> List[List[int]]:
        pascal=[]
        for i in range(1,numRows+1):
            each_row=[]
            for j in range(1,i+1):
                each_row.append(self.ncr(i-1,j-1))
            pascal.append(each_row)
        return pascal
