import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

# Bad way declare a class
# class PersonNoDataClass:
#     # <__main__.PersonNoDataClass object at 0x7ff727b1b0d0>
#     def __init__(self, name: str, address: str) -> None:
#         self.id = generate_id()
#         self.name = name
#         self.address = address
#         self.email_address = []


# kw_only (bool): Yeu cau phai khai bao cac truong khi khoi tao instance
# frozen (bool): Khong cho thay doi gia tri cua class
@dataclass
class Person:
    # init (bool): Xac dinh gia tri can khoi tao; repr (bool): xac dinh truong co duoc print ra khong
    name: str
    address: str
    id: str = field(default_factory=generate_id, init=False)
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name


def main() -> None:
    person = Person(name="John", address="123 Main St")
    # Return self.name: John
    print(person)
    print(f"{person}")
    # Return repr of class: Person(name='John', address='123 Main St', id='UNTWQYJIHZFX', active=True, email_addresses=[])
    print(repr(person))
    print(f"{person!r}")


if __name__ == '__main__':
    main()
