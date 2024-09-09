# Utility file for displaying wordle characters. Written by Daniel Kluver with support of various online documentation
#  ansii escape sequences. This stuff is archaic, but fun!


def green(letter):
    """Output one (or more) letters with a green background.
    This function produced no return value, prints to the screen, and does not print a newline character.
    """
    print("\033[42;1m", end="")
    print(letter, end="")
    print("\033[0m", end="")


def yellow(letter):
    """Output one (or more) letters with a yellow background.
    This function produced no return value, prints to the screen, and does not print a newline character.
    """
    print("\033[43;1m", end="")
    print(letter, end="")
    print("\033[0m", end="")


def grey(letter):
    """Output one (or more) letters with a grey background
    This function produced no return value, prints to the screen, and does not print a newline character.
    """

    print("\033[47;1m", end="")
    print(letter, end="")
    print("\033[0m", end="")


if __name__ == "__main__":
    grey("PIZZ")
    yellow("A")
    print()
    yellow("A")
    grey("PPL")
    green("E")
    print()
    yellow("S")
    grey("H")
    green("A")
    grey("D")
    green("E")
    print()
    yellow("S")
    grey("T")
    green("AGE")
    print()
    green("USAGE")
    print()
