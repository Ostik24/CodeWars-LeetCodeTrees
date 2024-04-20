def pre_order(node):
    result = []
    if node:
        head = node

        def visit(root):
            head = root
            result.append(head.data)
            if head.left:
                visit(head.left)
            if head.right:
                visit(head.right)

        visit(head)
    return result

def in_order(node):
    result = []
    if node:
        head = node

        def visit(root):
            head = root
            if head.left:
                visit(head.left)
            result.append(head.data)
            if head.right:
                visit(head.right)

        visit(head)
    return result


def post_order(node):
    result = []
    if node:
        head = node

        def visit(root):
            head = root
            if head.left:
                visit(head.left)
            if head.right:
                visit(head.right)
            result.append(head.data)

        visit(head)
    return result
