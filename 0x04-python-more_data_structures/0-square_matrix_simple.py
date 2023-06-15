#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix: A 2-dimensional array (default=[]).

    Returns:
        A new matrix with the squared values. Same size as the input matrix.

    """
    # Create a new matrix with the same size as the input matrix
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            # Compute the square of each value and add it to the new row
            new_row.append(value ** 2)
        # Add the new row to the result matrix
        result.append(new_row)

    return (result)
