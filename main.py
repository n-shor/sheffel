from structure import grammar, reductive


def main():
    # grammar.utils.regenerate()

    structure = reductive.Node()
    print(structure.hierarchy())


if __name__ == "__main__":
    main()
