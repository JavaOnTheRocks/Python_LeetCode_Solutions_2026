class Solution(object):
    def checkValid(self, matrix):
        n=len(matrix)

        for i in range(n):
            row_set=set()
            col_set=set()

            for j in range(n):
                col_val=matrix[i][j]
                row_val=matrix[j][i]
                
                if col_val<1 or row_val<1 or col_val>n or row_val>n:
                    return False

                row_set.add(row_val)
                col_set.add(col_val)

            if len(row_set) != n or len(col_set) != n:
                return False
        return True

         
        