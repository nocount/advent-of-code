# Day 6 AoC 2019

from anytree import Node, RenderTree, util, Walker

if __name__ == '__main__':

    with open('input.txt', 'r') as orbit_inputs:

        objects = {}
        for o in orbit_inputs.readlines():

            parsed = o.strip('\n').split(')')
            orbitee = parsed[0]
            orbiter = parsed[1]

            if orbitee not in objects:
                objects[orbitee] = Node(orbitee)

            if orbiter not in objects:
                objects[orbiter] = Node(orbiter, parent=objects[orbitee])
            else:
                objects[orbiter].parent = objects[orbitee]

        # Print tree structure
        # for pre, fill, node in RenderTree(objects['COM']):
        #     print("%s%s" % (pre, node.name))

        # Part 1
        orbits_sum = 0
        for obj in objects:
            orbits_sum += len(util.commonancestors(objects[obj]))

        # Part 2
        w = Walker()
        u, c, d = w.walk(objects['YOU'], objects['SAN'])
        min_jumps = len(u) + len(d) - 2

        print('Shortest path: ' + str(min_jumps) + ' jumps')
