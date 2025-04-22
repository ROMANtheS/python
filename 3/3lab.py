#Первая задача рекурсией
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

#Первая задача без рекурсии
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

#Вторая задача с рекурсией
def calculate_recursive(k, u, v):
    if k == 1:
        return (u, v)
    a_prev, b_prev = calculate_recursive(k - 1, u, v)
    a_k = 2 * b_prev + a_prev
    b_k = 2 * (b_prev ** 2) + b_prev
    return (a_k, b_k)

#Вторая задача без рекурсии
def calculate_iterative(k, u, v):
    a, b = u, v
    for _ in range(2, k + 1):
        a_new = 2 * b + a
        b_new = 2 * (b ** 2) + b
        a, b = a_new, b_new
    return (a, b)

test_obj = [1, 2, [3, 4, [5, [6, []]]]]

print("Рекурсивный поиск (Задача 1):")
print(f"find_recursive(test_obj, 4) = {find_recursive(test_obj, 4)}")  
print(f"find_recursive(test_obj, 6) = {find_recursive(test_obj, 6)}")  
print(f"find_recursive(test_obj, 'x') = {find_recursive(test_obj, 'x')}")  

print("\nИтеративный поиск (Задача 1):")
print(f"find_iterative(test_obj, 4) = {find_iterative(test_obj, 4)}")  
print(f"find_iterative(test_obj, 6) = {find_iterative(test_obj, 6)}")  
print(f"find_iterative(test_obj, 'x') = {find_iterative(test_obj, 'x')}")  

print("\nРекурсивный расчет (Задача 2):")
print(f"calc_recursive(3, 1, 1) = {calculate_recursive(3, 1, 1)}")  
print(f"calc_recursive(5, 1, 1) = {calculate_recursive(5, 1, 1)}")  

print("\nИтеративный расчет (Задача 2):")
print(f"calc_iterative(3, 1, 1) = {calculate_iterative(3, 1, 1)}")
print(f"calc_iterative(5, 1, 1) = {calculate_iterative(5, 1, 1)}")