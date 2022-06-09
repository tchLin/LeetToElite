class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc_tri=[]
        for i in range(numRows):
            if i == 0:
                pasc_tri.append([1])
            elif i == 1:
                pasc_tri.append([1, 1])
            else:
                temp=[]
                for j in range(i+1):
                    if j == 0:
                        temp.append(1)
                    elif j == i:
                        temp.append(1)
                    else:
                        temp.append(pasc_tri[i-1][j] + pasc_tri[i-1][j-1])
                pasc_tri.append(temp)
        return pasc_tri
