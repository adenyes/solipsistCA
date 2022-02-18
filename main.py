#!/bin/env python
ETERNITY = 256


def solipsist(cells: int) -> int:
    n2next = [(cells & 1 << n) >> n for n in reversed(range(8))]
    new_cells = 0
    for n in reversed(range(8)):
        new_cells = (new_cells << 1) | n2next[(cells << 1 >> n & 7)]
    return new_cells


def main():
    edges = set()
    max_lifespan = 0

    for world in range(256):
        new_world = solipsist(world)
        edges.add(f"\t{world} -> {new_world};\n")
        last_world = world
        lifespan = 0
        while lifespan < ETERNITY:
            new_world = solipsist(last_world)

            if new_world == last_world:
                if new_world != world:
                    max_lifespan = max(lifespan, max_lifespan)
                break
            last_world = new_world
            lifespan += 1

        if lifespan == ETERNITY:
            print(f"World {world} lasted eternally without 1-cycling.")

    print(f'Longest life before cycling was {max_lifespan}')

    with open('solipsistCA.dot', 'w') as fp:
        fp.write('digraph solipsistCA {\n')
        for e in edges:
            fp.write(e)
        fp.write('}')


if __name__ == '__main__':
    main()
