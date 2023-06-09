from typing import Generator


def cumulative(n: int) -> Generator[int, None, None]:
    total = 0
    for i in range(n):
        total += i
        yield total


def main() -> None:
    for i in cumulative(10):
        print(i)


if __name__ == "__main__":
    main()
