import sys
for line in sys.stdin:
    parts: list[str] = line.strip().split()
    if parts[0] == "END":
        exit()
    num1 = float(parts[0])
    num2 = float(parts[1])
    op: str = parts[2]
    solution = float(parts[3])
    correct: float = solution
    symbol: str = ""
    match op:
        case "SUBTRACT":
            correct = num1 - num2
            symbol = "-"
        case "ADD":
            correct = num1 + num2
            symbol = "+"
        case "MULTIPLY":
            correct = num1 * num2
            symbol = "*"
        case "DIVIDE":
            correct = num1 / num2
            symbol = "/"
    if "{:.1f}".format(solution) == "{:.1f}".format(correct):
        print("{:.1f} is correct for {:.1f} {} {:.1f}".format(solution,num1,symbol,num2))
    else:
        print("{:.1f} {} {:.1f} = {:.1f}, not {:.1f}".format(num1,str(symbol),num2,correct,solution))
    