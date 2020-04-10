from itertools import combinations_with_replacement, combinations, permutations

operators = ["+", "-", "*", "/"]
result, max_value = "", 0

operators_comb, current = [], []

def go(i):
    if i == 3:
        operators_comb.append(list(current))
    else:
        for item in operators:
            current.append(item)
            go(i + 1)
            current.pop()

def calculate(expression):
    stack = []
    for op in expression:
        try:
            if op in operators:
                if op == "+":
                    stack.append(stack.pop() + stack.pop())
                elif op == "-":
                    stack.append(stack.pop() - stack.pop())
                elif op == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    stack.append(stack.pop() / stack.pop())
            else:    
                stack.append(op)
        except ZeroDivisionError:
            return [False, None]
    if stack[0] > 0 and int(stack[0]) == stack[0]:
        return [True, stack[0]]
    else:
        return [False, None]

go(0)

for a in combinations([i for i in range(10)], 4):
    s = set()
    for order in permutations(a):
        for op_lst in operators_comb:
            cal_result = calculate([order[0], order[1], op_lst[0], order[2], op_lst[1], order[3], op_lst[2]])
            if cal_result[0]:
                s.add(cal_result[1])
            cal_result = calculate(list(order) + list(op_lst))
            if cal_result[0]:
                s.add(cal_result[1])
            cal_result = calculate([ order[0], order[1], order[2], op_lst[0], op_lst[1], order[3], op_lst[2]])
            if cal_result[0]:
                s.add(cal_result[1])
    i = 1
    while i in s:
        i += 1
    if i > max_value:
        result, max_value = "".join(map(str, sorted(a))), i
    
print(result)
