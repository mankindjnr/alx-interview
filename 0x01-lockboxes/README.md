# Solution: Can Unlock All Boxes

This repository contains a solution for the task of determining whether all the boxes in a given set can be opened. The task involves a list of locked boxes, each numbered sequentially from 0 to n - 1, where each box may contain keys to other boxes. The objective is to write a method that determines if all the boxes can be opened.

## Method

The solution provides a method called `canUnlockAll(boxes)`, which takes a list of lists (`boxes`) as its input. The method follows the specified prototype and returns a Boolean value.

### Input

The input parameter `boxes` represents the set of locked boxes. It is a list of lists, where each inner list represents a box. The index of each inner list corresponds to the box number, and the values within the inner lists represent the keys contained within the respective box. The following assumptions are made about the input:

- All keys are positive integers.
- There can be keys that do not have corresponding boxes.
- The first box, `boxes[0]`, is initially unlocked.

### Output

The `canUnlockAll()` method returns `True` if all the boxes can be opened, indicating that it is possible to unlock every box in the given set. If there are any boxes that cannot be opened, the method returns `False`.

### Approach

The solution utilizes a depth-first search (DFS) algorithm to explore the relationships between the boxes and their respective keys. It starts by initializing a list called `visited_boxes` to keep track of the boxes that have been visited during the search process. Initially, only the first box (`boxes[0]`) is marked as visited.

The algorithm then proceeds to visit each box sequentially and examines the keys it contains. If a key corresponds to a box that has not been visited yet, that box is marked as visited, and the algorithm recursively explores its keys. This process continues until either all the boxes have been visited or no further unvisited boxes can be unlocked.

Finally, the algorithm checks whether all the boxes have been visited. If so, it returns `True`, indicating that all boxes can be opened. Otherwise, it returns `False`.

## Usage

To use the solution, follow these steps:

1. Ensure you have a compatible Python environment set up.
2. Clone or download this repository.
3. Include the `canUnlockAll()` method in your code.
4. Call the `canUnlockAll()` method, passing in the list of boxes as the argument.
5. Receive the Boolean result indicating whether all boxes can be opened.

Example usage:

```python
# Import the solution method
from unlock_boxes import canUnlockAll

# Define the locked boxes
boxes = [[1], [2], [3], []]

# Check if all boxes can be opened
result = canUnlockAll(boxes)
print(result)  # Output: True
