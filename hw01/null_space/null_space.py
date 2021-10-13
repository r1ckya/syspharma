from sympy import Matrix


def main():
    N = Matrix(
        [[1, -1, 0, 0, -1, 0], [0, 1, -1, 0, 0, 0], [0, 0, 1, -1, 0, 1]]
    )
    for v in N.nullspace():
        print(*v)


if __name__ == "__main__":
    main()
