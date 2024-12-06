def several_zeros():
    return [0 for i in range(10)]

def several_zeros_custom(nb_zeros = 10):
    return [0 for i in range(nb_zeros)]

def matrix(rows, cols):
    return [[0 for i in range(cols)] for j in range(rows)]

class Matrix:

    matrix = []


    def __init__(self, rows, cols):
        self.matrix = [[0 for i in range(cols)] for j in range(rows)]


    def get_value(self, row, col):
        return self.matrix[row][col]


    def __eq__(self, other):
        return self.matrix == other.matrix




def my_sort(my_list: [int]) -> [int]:
    """
    Bubble sort algorithm
    """
    n = len(my_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

