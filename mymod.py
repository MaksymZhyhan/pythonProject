def count_lines(name):
    with open(name, "r") as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, "r") as file:
        chars = file.read()
        return len(chars)


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"(Lines: {lines}")
    print(f"Characters: {chars}")


if __name__ == "__main__":
    test("mymod.py")
