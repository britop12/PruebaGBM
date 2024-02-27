def reachX(input_lines):
    input_lines = list(map(int, input_lines.strip().split("\n")))


    t = input_lines[0]
    cases = input_lines[1:]
    output = []

    for x in cases:
        sum_jumps, jumps = 0, 0
        while sum_jumps < x:
            jumps += 1
            sum_jumps += jumps
            # print(sum_jumps, jumps)

        if sum_jumps - x == 1:
            jumps += 1
        output.append(jumps)
    return "\n".join(map(str, output))

