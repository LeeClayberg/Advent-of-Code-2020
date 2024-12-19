# Read in stuff
with open("files/day17.txt", "r") as file_stream:
    # Setup
    registers, program = file_stream.read().split('\n\n')
    # a, b, c = [int(register.split(' ')[-1]) for register in registers.split('\n')]
    program = [int(p) for p in program[:-1].split(' ')[-1].split(',')]

    for start_a in range(100000000, 1000000000): # 223345489
        print(start_a)
        a, b, c = start_a, 0, 0

        def combo(op):
            if op <= 3:
                return op
            elif op == 4:
                return a
            elif op == 5:
                return b
            elif op == 6:
                return c


        output = []
        ip = 0
        while ip < len(program):
            opcode = program[ip]
            ip += 1
            operand = program[ip]
            ip += 1

            if opcode == 0: # adv
                a = a // pow(2, combo(operand))
            elif opcode == 1: # bxl
                b = b ^ operand
            elif opcode == 2:  # bst
                b = combo(operand) % 8
            elif opcode == 3: # jnz
                if a != 0:
                    ip = operand
            elif opcode == 4: # bxc
                b = b ^ c
            elif opcode == 5: # out
                mod = combo(operand) % 8
                if mod != program[len(output)]:
                    break
                output.append(mod)
            elif opcode == 6: # bdv
                b = a // pow(2, combo(operand))
            elif opcode == 7: # cdv
                c = a // pow(2, combo(operand))

        if output == program:
            print(start_a)
            break

