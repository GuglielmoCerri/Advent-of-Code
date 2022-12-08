import lib.aoc as aoc
import numpy as np

def get_matrix_position(data:str) -> np.matrix:
    data = data.split('\n')
    matrix = np.matrix([ [int(j) for j in i] for i in data ])
    positions = [ (i,j) for i in range(len(matrix)) \
                   for j in range(len(matrix)) if i > 0 and j > 0 and j < len(matrix)-1 and i < len(matrix)-1]
    
    return matrix, positions

#-------------------------------------------------------------------------------    
@aoc.main('08', 1)
def main_p1(indata: str) -> str:
    
    matrix, positions = get_matrix_position(indata)

    visible_edge_trees  = pow(len(matrix), 2) - len(positions)
    visible_inner_trees = [] 
    for pos in positions:
        i,j = pos
        
        row_left  = matrix[i, :j]
        row_right = matrix[i, j+1:]
        col_down  = matrix[i+1:,j]
        col_up    = matrix[:i,j]
        
        row_cond  = (matrix[i,j] > max(row_left.tolist()[0]) or 
                     matrix[i,j] > max(row_right.tolist()[0]))

        col_cond  = (matrix[i,j] > max(col_down.flatten().tolist()[0]) or 
                     matrix[i,j] > max(col_up.flatten().tolist()[0]))
                                                                              
        visible_inner_trees.append(row_cond or col_cond)

    return sum(visible_inner_trees) + visible_edge_trees

#-------------------------------------------------------------------------------    
@aoc.main('08', 2)
def main_p2(indata: str) -> str:
    matrix, positions = get_matrix_position(indata)

    scores = []

    for pos in positions:
        l = r = u = d = 0
        a, b = pos
        
        row_left  = matrix[a, :b] ; row_left = row_left.tolist()[0]
        row_left.reverse()
        row_right = matrix[a, b+1:] ; row_right = row_right.tolist()[0]
        col_down  = matrix[a+1:,b]  ; col_down = col_down.flatten().tolist()[0]
        col_up    = matrix[:a,b]    ; col_up = col_up.flatten().tolist()[0]
        col_up.reverse()
        
        for i in col_up:
            u += 1
            if i >= matrix[a,b]: break
        
        for i in row_left:
            l += 1
            if i >= matrix[a,b]: break
            
        for i in col_down:
            d += 1
            if i >= matrix[a,b]: break
            
        for i in row_right:
            r += 1
            if i >= matrix[a,b]: break
            
        scores.append(l * r * u * d)

    return max(scores)

if __name__ == "__main__":
    main_p1()
    main_p2()