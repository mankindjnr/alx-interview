#!/usr/bin/python3
"""
representation of the pascal's triangle
"""
def pascal_triangle(n):
    """
    this function returns a list of lists of integers 
    """
    major = []
    if n <= 0:
        return major
    else:
        for i in range(n):
            a_list = []
            break_flag = False

            major_len = len(major)
            for j in range(n - (n-(i+1))):
                if major_len < 2:
                    if i > 0:   
                        a_list.append(i)
                    else:
                        a_list.append(i+1)
                else:
                    a_list.append(1)
                    list_idx = major_len - 1
                    list_len = len(major[list_idx])
                    the_list = major[list_idx]

                    for tri in range(list_len - 1):
                        a_list.append(the_list[tri] + the_list[tri + 1])

                    a_list.append(1)
                    break
            
            major.append(a_list)
        
        return major

