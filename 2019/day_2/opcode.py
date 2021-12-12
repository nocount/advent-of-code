# Day 2 of Advent of Code 2019


def run_grav_assist(program, noun, verb):

    temp_program = program.copy()
    temp_program[1] = noun
    temp_program[2] = verb

    index = 0
    while 1:

        if temp_program[index] == 1:
            # Add
            temp_program[temp_program[index + 3]] = temp_program[temp_program[index + 1]] + temp_program[temp_program[index + 2]]
            index += 4

        if temp_program[index] == 2:
            # Multiply
            temp_program[temp_program[index + 3]] = temp_program[temp_program[index + 1]] * temp_program[temp_program[index + 2]]
            index += 4

        if temp_program[index] == 99:
            break

    return temp_program[0]


if __name__ == '__main__':

    with open('input.txt', 'r') as input:

        parsed_input = [int(numeric_string) for numeric_string in input.readline().split(',')]

        for n in range(0, 99):
            for v in range(0, 99):

                output = run_grav_assist(parsed_input, n, v)

                print('N: ' + str(n) + ' V: ' + str(v) + ' Out: ' + str(output))
                if output == 19690720:
                    print('Ay Caramba AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH Noun: ' + str(n) + ' Verb: ' + str(v))
                    break
            else:
                continue
            break
