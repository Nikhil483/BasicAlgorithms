from StacksAndQueues.CustomStack import Stack

bracket_map = {'(':')', '{':'}', '[':']'}
open_bracket = bracket_map.keys()
close_bracket = bracket_map.values()

def check_if_balanced(exp):
    n = len(exp)
    s = Stack(n)
    index = 0

    while index < n :
        if exp[index] in open_bracket:
            s.push(exp[index])
        elif exp[index] in close_bracket:
            element = s.pop()
            if exp[index] == bracket_map[element] :
                index += 1
                continue
            else :
                return False
        index += 1
    return True

if __name__ == "__main__" :
    balanced = "([]){}"
    unbalanced = "[]({)}[]"

    if check_if_balanced(balanced):
        print(balanced + " is balanced")
    else :
        print(balanced + " is not balanced")

    if check_if_balanced(unbalanced):
        print(unbalanced + " is balanced")
    else :
        print(unbalanced + " is not balanced")

