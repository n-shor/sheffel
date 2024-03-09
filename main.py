from structure import grammar, pure


def main():
    grammar.utils.regenerate()

    structure = pure.Node()
    print(structure.hierarchy())


if __name__ == "__main__":
    main()
