def reachX(input_lines):
    input_lines = list(map(int, input_lines.strip().split("\n")))

    t = input_lines[0]
    cases = input_lines[1:]
    output = []

    for x in cases:
        sum_jumps, jumps = 0, 0
        # add jumps until the sum of jumps is greater than or equal to x
        while sum_jumps < x:
            jumps += 1
            sum_jumps += jumps
            # print(sum_jumps, jumps)
        # if the difference is 1, we need to add an extra jump
        if sum_jumps - x == 1:
            jumps += 1
        output.append(jumps)
    return "\n".join(map(str, output))

if __name__ == "__main__":
    input_lines = ""
    t = int(input("Ingresa el número de casos de prueba: \n"))
    input_lines += str(t) + "\n"
    for _ in range(t):
        input_lines += input("Ingresa el valor de x: \n") + "\n"
    print("Output:")
    print(reachX(input_lines))


