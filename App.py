
i = input("first Number: ")                    # i = input("First Number: "
u = input("(+, -, *, /, =: ")                    # u = input("Operator (+, -, *, /, =: ")

while u != "=":

    if u == "+":
        o = input("Second Number: ")
        i = (float(i) + float(o))

    elif u == "-":
        o = input("Second Number: ")
        i = (float(i) - float(o))

    elif u == "*":
        o = input("Second Number: ")
        i = (float(i) * float(o))

    elif u == "/":
        o = input("Second Number: ")
        i = (float(i) / float(o))

    print("Answer: ")
    print(i)
    u = input("(+, -, *, /, =): ")

