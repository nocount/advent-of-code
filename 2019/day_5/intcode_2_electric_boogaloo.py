# Day 5 Advent of Code 2019


def execute_intcode(code):
    temp_code = code
    index = 0
    while 1:

        instruction = str(temp_code[index])
        while len(instruction) < 5:
            instruction = '0' + instruction
        opcode = int(instruction[3:5])

        if opcode == 1:
            # Add
            in_1 = temp_code[index+1] if instruction[2] == '1' else temp_code[temp_code[index+1]]
            in_2 = temp_code[index+2] if instruction[1] == '1' else temp_code[temp_code[index+2]]
            temp_code[temp_code[index + 3]] = in_1 + in_2
            index += 4

        if opcode == 2:
            # Multiply
            in_1 = temp_code[index + 1] if instruction[2] == '1' else temp_code[temp_code[index + 1]]
            in_2 = temp_code[index + 2] if instruction[1] == '1' else temp_code[temp_code[index + 2]]
            temp_code[temp_code[index + 3]] = in_1 * in_2
            index += 4

        if opcode == 3:
            # Input
            val = int(input('Enter input: '))
            temp_code[temp_code[index + 1]] = val
            index += 2

        if opcode == 4:
            # Output
            out_1 = temp_code[index+1] if instruction[2] == '1' else temp_code[temp_code[index+1]]
            print(out_1)
            index += 2

        if opcode == 5:
            # Jump if True
            in_1 = temp_code[index + 1] if instruction[2] == '1' else temp_code[temp_code[index + 1]]
            in_2 = temp_code[index + 2] if instruction[1] == '1' else temp_code[temp_code[index + 2]]
            if in_1 != 0:
                index = in_2
            else:
                index += 3

        if opcode == 6:
            # Jump if False
            in_1 = temp_code[index + 1] if instruction[2] == '1' else temp_code[temp_code[index + 1]]
            in_2 = temp_code[index + 2] if instruction[1] == '1' else temp_code[temp_code[index + 2]]
            if in_1 == 0:
                index = in_2
            else:
                index += 3

        if opcode == 7:
            # Less than
            in_1 = temp_code[index + 1] if instruction[2] == '1' else temp_code[temp_code[index + 1]]
            in_2 = temp_code[index + 2] if instruction[1] == '1' else temp_code[temp_code[index + 2]]
            if in_1 < in_2:
                temp_code[temp_code[index+3]] = 1
            else:
                temp_code[temp_code[index+3]] = 0
            index += 4

        if opcode == 8:
            # Equals
            in_1 = temp_code[index + 1] if instruction[2] == '1' else temp_code[temp_code[index + 1]]
            in_2 = temp_code[index + 2] if instruction[1] == '1' else temp_code[temp_code[index + 2]]
            if in_1 == in_2:
                temp_code[temp_code[index + 3]] = 1
            else:
                temp_code[temp_code[index + 3]] = 0
            index += 4

        if int(opcode) == 99:
            break


if __name__ == '__main__':

    with open('input.txt', 'r') as input_code:

        code = [int(numeric_string) for numeric_string in input_code.readline().split(',')]

        # code = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        execute_intcode(code)
