from console import Console

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        code = file.read()

    console = Console()
    print("Part 1:", console.run(code))
    print("Part 2:", console.fix_loop_and_run(code))
