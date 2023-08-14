def compare_brackets(current, last):
    if current == ')' and last == '(':
        return True
    elif current == ']' and last == '[':
        return True
    elif current == '}' and last == '{':
        return True
    return False


def check_seq(seq_brackets):
    stack = []
    for bracket in seq_brackets:
        if not stack:
            stack.append(bracket)
            continue
        if bracket in ('(', '[', '{'):
            stack.append(bracket)
        elif compare_brackets(bracket, stack[-1]):
            stack.pop()
    return not stack


def main():
    seq_brackets = input().strip()
    print(check_seq(seq_brackets))


if __name__ == "__main__":
    main()
