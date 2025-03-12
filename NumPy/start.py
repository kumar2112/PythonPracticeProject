# import time

# # Create a list of 1 million integers
# python_list = list(range(1, 1000001))

# # Measure the time taken to sum the elements of the list
# start_time = time.time()
# sum_list = sum(python_list)
# end_time = time.time()

# print(f"Time taken to sum the Python list: {end_time - start_time} seconds")


import numpy as np

arr = np.array([
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [6, 7, 8, 9, 10]
                
               ])

print(arr.shape)

