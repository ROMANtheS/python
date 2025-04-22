def find_recursive(obj, target, index=None):
    if index is None:
        index = []
    if obj == target:
        return index.copy()
    if isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            index.append(i)
            result = find_recursive(item, target, index)
            if result is not None:
                return result
            index.pop()
    return None

def find_iterative(obj, target):
    stack = [(obj, [])]
    while stack:
        current_obj, path = stack.pop()
        if current_obj == target:
            return path
        if isinstance(current_obj, (list, tuple)):
            for i in reversed(range(len(current_obj))):
                stack.append((current_obj[i], path + [i]))
    return None

def calculate_recursive(k, u, v):
    if k == 1:
        return (u, v)
    a_prev, b_prev = calculate_recursive(k - 1, u, v)
    a_k = 2 * b_prev + a_prev
    b_k = 2 * (b_prev ** 2) + b_prev
    return (a_k, b_k)

def calculate_iterative(k, u, v):
    a, b = u, v
    for _ in range(2, k + 1):
        a_new = 2 * b + a
        b_new = 2 * (b ** 2) + b
        a, b = a_new, b_new
    return (a, b)
print("Задача 1 (рекурсией):", find_recursive())
print("Задача 1 (без рекурсии):", find_iterative())
print("Задача 2 (рекурсией): ", calculate_recursive())
print("Задача 2 (без рекурсии): ", calculate_iterative())