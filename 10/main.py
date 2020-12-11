def compute_differences(adapters: [int]) -> [int]:
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    differences = []
    currrent_joltage = 0
    for adapter in adapters:
        difference = adapter - currrent_joltage
        differences.append(difference)
        currrent_joltage = adapter
    return differences


def _get_init_dict(adapters: [int]) -> dict[int, int]:
    init_dict = dict()
    for adapter in adapters:
        init_dict[adapter] = 0
    return init_dict


def compute_paths(adapters: [int]) -> dict[int, int]:
    adapters.sort()
    # make sure powerplug is included
    adapters.insert(0, 0)
    # amount of paths that lead to specific adapter
    paths = _get_init_dict(adapters)
    # there's only one way to the first adapter
    paths[0] = 1
    for i in range(len(adapters)):
        for offset in range(1, 4):
            if adapters[i] + offset in adapters:
                paths[adapters[i] + offset] += paths[adapters[i]]
    return paths


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        adapters = file.read().splitlines()
        adapters = [int(x) for x in adapters]

    differences = compute_differences(adapters)
    print("Part 1:", differences.count(1) * differences.count(3))

    paths = compute_paths(adapters)
    print("Part 2:", list(paths.values())[-1])
