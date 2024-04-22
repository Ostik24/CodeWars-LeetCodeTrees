from collections import deque

def tree_by_levels(node):
    result = []
    if node:
        my_queue = deque()

        result.append(node.value)
        my_queue.append(node)

        while my_queue:
            popped = my_queue.popleft()
            if popped.left:
                my_queue.append(popped.left)
                result.append(popped.left.value)
            if popped.right:
                my_queue.append(popped.right)
                result.append(popped.right.value)

    return result
