from lib.aoc import aoc

def run_program(registers, program):
    def combo_operand(value):
        match value:
            case 0 | 1 | 2 | 3:
                return value
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C

    A, B, C = registers
    pointer = 0
    outputs = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:  # adv
            A //= 2 ** combo_operand(operand)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = combo_operand(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                pointer = operand
                continue  # skip the pointer increment
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            outputs.append(combo_operand(operand) % 8)
        elif opcode == 6:  # bdv
            B = A // (2 ** combo_operand(operand))
        elif opcode == 7:  # cdv
            C = A // (2 ** combo_operand(operand))

        pointer += 2

    return outputs

@aoc(17, 2024, 1)
def p1(indata: str):
    data = indata.strip().splitlines()
    registers = [
            int(data[0].split(": ")[1]),
            int(data[1].split(": ")[1]),
            int(data[2].split(": ")[1]),
        ]
    program = list(map(int, data[4].split(": ")[1].split(",")))

    result = run_program(registers, program)
    return ",".join(map(str, result))

@aoc(17, 2024, 2)
def p2(indata: str):
    data = indata.strip().splitlines()
    program = list(map(int, data[4].split(": ")[1].split(",")))
    A = sum(7 * 8**i for i in range(len(program) - 1)) + 1

    while True:
        result = run_program([A, 0, 0], program)

        if len(result) > len(program):
            raise ValueError("The output is too long")

        if result == program:
            return A

        add = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] != program[i]:
                add = 8**i
                A += add
                break


if __name__ == "__main__":
    p1()
    p2()
