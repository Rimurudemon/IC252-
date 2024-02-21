import numpy as np

mat = np . array ([[1 ,3 ,4 ,5 ,2] ,[1 ,5 ,2 ,4 ,3] ,[5 ,2 ,3 ,4 ,1 ,] ,[1 ,4 ,2 ,6 ,9] ,[4 ,5 ,2 ,1 ,7]])

#------------------------------{part 1}-------------------------------------------

def left_diagonal_sum ( mat : np . ndarray ) ->float :
        sum = 0
        for i in range(0,5):
            for j in range(0,5):     
                if i == j:
                    sum+=mat[i][j]

                else:
                    pass
        return sum
        pass
def right_diagonal_sum ( mat : np . ndarray ) ->float :
        sum = 0
        for i in range(0,5):
            for j in range(4,-1,-1):     
                if i+j == 4:
                    sum+=mat[i][j]

                else:
                    pass
        return sum
        pass

print (f'Left Diagonal Sum of { mat =} is { left_diagonal_sum (mat)}')
print (f'Right Diagonal Sum of { mat =} is { right_diagonal_sum ( mat )}')

# --.----------------------------{part 2}-------------------------------------------
def submatrix_3x4 ( mat : np . ndarray ) -> np . ndarray :
        submat= mat[0:3,1:5]
        return submat
        pass
print (f'The desired submatrix of \n { mat } is \n { submatrix_3x4 ( mat )}')