my_str: str = 'Hello World'
my_list: list[int] = [34, 54, 65, 78]
my_dict: dict[str, int] = {'one': 123, 'two': 456, 'three': 789}

print(len(my_str))
print(len(my_list))
print(len(my_dict))

class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages
    
print(len(Book("J.K", "Way back home", 542)))
book: Book = Book("Thanh", "My Love", 258)