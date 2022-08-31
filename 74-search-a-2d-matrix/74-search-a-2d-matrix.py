class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        h = len(matrix) - 1 
        
        while l <= h :
            m = (l+h) // 2
            if (matrix[m][0] > target ) :
                h = m - 1
            if (matrix[m][0] < target ) :
                l = m + 1
            if matrix[m][0] == target :
                return True
            
            l1 = 0
            h1 = len(matrix[0]) - 1 
        
            while l1 <= h1:
                m1 = (l1+h1) // 2
                if (matrix[m][m1] > target ) :
                    h1 = m1 - 1
                elif (matrix[m][m1] < target ) :
                    l1 = m1 + 1
                else :
                    return True

                
    
    
        
        return False
        
        