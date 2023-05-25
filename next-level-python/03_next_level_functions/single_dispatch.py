from functools import singledispatch
from typing import Union


@singledispatch
def add() -> ...:
    ...


@add.register(int)
def _(x: int, y: int) -> int:
    return x + y


@add.register(str)
def _(x: str, y: str) -> str:
    return f"{x} {y}"


# you can also use the union type
@add.register(list)
@add.register(set)
@add.register(type(None))
def _(x: Union[list[object], set[object]], y: list[object] | set[object]) -> list[object]:
    return [*x, *y]


# functional form
add.register(tuple, lambda x, y: (*x, *y))


def main() -> None:
    print(add(1, 2))
    print(add("Hello", "World"))
    print(add(["Hello", 2, 3], ["Hello", 5, 6]))
    print(add({"Hello", 2, 3}, {4, 5, 6}))
    print(add(("Hello", 2, 3), ("Hello", 5, 6)))
    print(add(("Hello", 2, 3), ("Hello", 5, 6)))


if __name__ == "__main__":
    main()
