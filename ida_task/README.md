
# Smallest Positive Integer

This folder contains the solution for finding the smallest positive integer that does not occur in an array of N integers.

## Task Description

The task is to write a function that takes an array of N integers and returns the smallest positive integer (> 0) that does not occur in the given array.

### Example

```python
Input: [1, 3, 6, 4, 1, 2]
Output: 5

Input: [1, 2, 3]
Output: 4

Input: [-1, -3]
Output: 1
```

## Assumptions

- N is an integer within the range: [1...100,000]
- Each element of the array is an integer within the range: [-1,000,000, 1,000,000]

## Files

- `solution.py`: Contains the implementation of the function to find the smallest positive integer.
- `test_solution.py`: Includes unit tests to verify the correctness of the solution.

## Usage

1. Make sure you have Python installed on your system.
2. Open the terminal and navigate to the folder containing the solution files.
3. Run the tests by executing the following command:

   ```bash
   python test_solution.py
   ```

   This will run the unit tests and display the results.

4. You can also import the `solution` module into your own Python script and use the `find_smallest_positive_integer` function by following these steps:

   ```python
   from solution import find_smallest_positive_integer

   array = [1, 3, 6, 4, 1, 2]
   result = find_smallest_positive_integer(array)
   print(result)
   ```

   This will output the smallest positive integer that does not occur in the given array.

Feel free to modify and extend the solution or add your own test cases as needed.

**Note:** Please ensure that you have properly set up your Python environment and have the necessary dependencies installed before running the solution or tests.

Happy coding!