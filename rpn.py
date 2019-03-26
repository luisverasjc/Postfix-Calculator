def main():
    # Inputs will be integers
    stack = []
    while True:
        try:
            s = input()
        except EOFError:
            return
        if s is "~": #negate
            a = stack.pop()
            c = a * -1
            stack.append(c)
            print(c)
        elif s in "+/-*":
            if len(stack) < 2:
                print("invalid operation")
            else:
                a = stack.pop()
                b = stack.pop()
                if s == "+":
                    c = b + a
                elif s == "-":
                    c = b - a
                elif s == "/":
                    if a != 0:
                        c = b / a
                    else:
                        print("error: divide by 0")
                elif s == "*":
                    c = b * a
                stack.append(c)
                print(c)
        else:
            print(s)
            stack.append(float(s))

if __name__ == '__main__':
    main()
