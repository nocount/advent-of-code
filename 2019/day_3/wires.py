# Advent of Code 2019 Day 3


def run_wire(wire):

    coordinates = {}
    x_start = y_start = steps = 0
    x_index = x_start
    y_index = y_start

    for command in wire:
        direction = command[0:1]
        distance = int(command[1:])
        for j in range(0, distance):
            if direction == 'R':
                x_index += 1
            elif direction == 'L':
                x_index -= 1
            elif direction == 'U':
                y_index += 1
            elif direction == 'D':
                y_index -= 1

            steps += 1

            if (x_index, y_index) not in coordinates:
                coordinates[(x_index, y_index)] = steps

    return coordinates


if __name__ == '__main__':

    with open('input.txt', 'r') as input:

        wire1 = input.readline().split(',')
        wire1 = [s.strip('\n') for s in wire1]
        wire2 = input.readline().split(',')
        wire2 = [s.strip('\n') for s in wire2]

        wire1_coordinates = run_wire(wire1)
        wire2_coordinates = run_wire(wire2)

        intersection_coordinates = [coord for coord in wire1_coordinates if coord in wire2_coordinates]

        # Part 1
        min_distance = min(abs(x) + abs(y) for (x, y) in intersection_coordinates)
        print(min_distance)

        # Part 2
        shortest_steps = min(wire1_coordinates[coord] + wire2_coordinates[coord] for coord in intersection_coordinates)
        print(shortest_steps)