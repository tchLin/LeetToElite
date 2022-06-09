class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r*c != len(mat[0])*len(mat):
            return mat

        new_mat=[[]*c for i in range(r)]
        
        new_col_cntr=0
        new_row_pntr=0
        old_col_pntr=0
        old_row_pntr=0
        
        while new_row_pntr < r:
            if new_col_cntr != c:
                print(old_col_pntr, old_row_pntr)
                new_mat[new_row_pntr].append(mat[old_row_pntr][old_col_pntr])
                new_col_cntr+=1
                old_col_pntr+=1       
            else:
                new_col_cntr=0
                new_row_pntr+=1
            
            if old_col_pntr == len(mat[0]):
                old_col_pntr=0
                old_row_pntr+=1
        
        return new_mat
