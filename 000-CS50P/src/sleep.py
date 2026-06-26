def main():
    n: int = int(input("Number: "))
    for s in sheeps(n):
        print(s)


# def sheeps(n):
#     flock: list = []
#     for counting in range(n):
#         flock.append("🐑" * counting)
#     return flock


def sheeps(n):
    for i in range(n):
        line: str = "🐑" * i
        yield line


if __name__ == "__main__":
    main()
