import numpy as np

def flippingMatrix(matrix):
    # Write your code here
    if len(matrix) == 0:
        # Handle empty matrix
        return 0
        
    side_len = len(matrix[0])
    
    # we know that the matrix has size 2n x 2n. Thus, the
    # top-left quadrant has size nxn
    n = int(side_len / 2)
    
    # The full matrix is divided into 4 quadrants: top-left, top-right, bottom-left, bottom-right
    # Let's look for potential improvements of the top-left quadrant by comparing it with the other quadrants
    # by the order specified above.
    
    matrix = np.array(matrix)
    
    
    # ====================================================================
    # Check for changes between top-left and top-right quadrants
    top_left_matrix = matrix[:n, :n]    # Get the top-left matrix
    top_right_matrix = matrix[:n, n:]   # Get the top-right matrix
    # Compare each row of the 2 matrices
    for row_idx in range(n):
        top_left_row = top_left_matrix[row_idx, :]
        top_right_row = top_right_matrix[row_idx, :]
        
        if sum(top_right_row) > sum(top_left_row):
            # Reverse the row to include the top_right_row instead
            matrix[row_idx, :] = matrix[row_idx, ::-1]
        
        # Else, do nothing
    
    # ====================================================================
    # Check for changes between top-left and bottom-left quadrants
    top_left_matrix = matrix[:n, :n]    # Get the top-left matrix
    bottom_left_matrix = matrix[n:, :n]   # Get the bottom-left matrix
    # Compare each column of the 2 matrices
    for col_idx in range(n):
        top_left_col = top_left_matrix[:, col_idx]
        bottom_left_col = bottom_left_matrix[:, col_idx]
        
        if sum(bottom_left_col) > sum(top_left_col):
            # Reverse the column to include the bottom_left_col instead
            matrix[:, col_idx] = matrix[::-1, col_idx]
        
        # Else, do nothing
        
    # ====================================================================
    # Check for changes between top-left and bottom-left quadrants
    top_left_matrix = matrix[:n, :n]    # Get the top-left matrix
    bottom_right_matrix = matrix[n:, n:]   # Get the bottom-left matrix
    # Compare each column or row of the 2 matrices
    
    # Compare each row of the 2 matrices
    for row_idx in range(n):
        top_left_row = top_left_matrix[row_idx, :]
        bottom_right_row = bottom_right_matrix[row_idx, :]
        
        if sum(bottom_right_row) > sum(top_left_row):
            # Reverse the row and column
            # 1. Reverse the columns
            for col_idx in range(n, 2*n, 1):
                # Reverse the cols of the bottom_right_matrix
                matrix[:, col_idx] = matrix[::-1, col_idx]
                
            # 2. Reverse the row to add the higher sum to the top-left matrix
            matrix[row_idx, :] = matrix[row_idx, ::-1]
        
        # Else, do nothing
    for col_idx in range(n):
        top_left_col = top_left_matrix[:, col_idx]
        bottom_right_col = bottom_right_matrix[:, col_idx]
        
        if sum(bottom_right_col) > sum(top_left_col):
            # Reverse the row and column
            # 1. Reverse the rows
            for row_idx in range(n, 2*n, 1):
                # Reverse the rows of the bottom_right_matrix
                matrix[row_idx, :] = matrix[row_idx, ::-1]
                
            # 2. Reverse the column to add the higher sum to the top-left matrix
            matrix[:, col_idx] = matrix[::-1, col_idx]
        
        # Else, do nothing
        
    # Calculate sum of the top-left matrix
    top_left_matrix = matrix[:n, :n]    # Get the top-left matrix
    
    sum_elems = np.sum(top_left_matrix)
    
    print("top_left_matrix:", top_left_matrix)
    
    return sum_elems


def flippingMatrix2(matrix):
    # Write your code here
    if len(matrix) == 0:
        # Handle empty matrix
        return 0
        
    side_len = len(matrix[0])
    
    # we know that the matrix has size 2n x 2n. Thus, the
    # top-left quadrant has size nxn
    n = int(side_len / 2)
    
    # The full matrix is divided into 4 quadrants: top-left, top-right, bottom-left, bottom-right
    # Let's look for potential improvements of the top-left quadrant by comparing it with the other quadrants
    # by the order specified above.
    
    matrix = np.array(matrix)
    
    
    # ====================================================================
    # Check for the best elements for each position in the top-left matrix
    for row_idx in range(n):
        for col_idx in range(n):
            # Check which possible elem is the max
            possible_vals = [
                matrix[row_idx, col_idx], matrix[row_idx, n-col_idx], 
                matrix[n-row_idx, col_idx], matrix[n-row_idx, n-col_idx]
            ]
            
            # Returns the index of the element with highest value
            max_idx = np.argmax(possible_vals)
            max_val = possible_vals[max_idx]

            """ if max_idx == 0:
                # Do nothing since the max value is already at top-right
                continue
            elif max_idx == 1:
                # Switch the top-right elem with the top-left elem -- Row Inversion
                matrix[row_idx, :] = matrix[row_idx, ::-1]
            elif max_idx == 2:
                # Switch the bottom-left elem with the top-left elem -- Column Inversion
                matrix[:, col_idx] = matrix[::-1, col_idx]
            elif max_idx == 3:
                # Switch the bottom-right elem with the top-left elem -- Row and Column Inversion
                # 1. Reverse the column
                matrix[:, col_idx] = matrix[::-1, col_idx]

                # 2. Reverse the row to add the higher sum to the top-left matrix
                matrix[row_idx, :] = matrix[row_idx, ::-1]
            else:
                # Unexpected value
                raise ValueError("Unexpected value for max_idx") """
            
            # Replace the elem at the top-left with the max_val
            matrix[row_idx, col_idx] = max_val

    # Calculate sum of the top-left matrix
    top_left_matrix = matrix[:n, :n]    # Get the top-left matrix

    sum_elems = np.sum(top_left_matrix)

    print("top_left_matrix:", top_left_matrix)

    return sum_elems
            
           
            
