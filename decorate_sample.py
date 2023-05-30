
from fastapi import FastAPI


from functools import wraps
from typing import Callable, Any

app = FastAPI()


def middleware(func: Callable[[Any, Any], Any]):
    @wraps(func)
    def decorated_function(*args: Any, **kwargs: Any) -> Callable[[Any, Any], Any]:
        print("Anythings are here")
        print('*args', args)
        print('**kwargs', kwargs)
        return func(*args, **kwargs)  # type: ignore

    return decorated_function


def user_is(role: str) -> Callable[[Any], Any]:
    def wrapper(func: Callable[[str], Any]) -> Callable[[], Any]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Callable[[], Any]:
            print("Anythings are here")
            print('*args', args)
            print('**kwargs', kwargs)
            # type: ignore
            return func(*args, **kwargs)
        return inner
    return wrapper


@middleware
@user_is("aaaaaaaaaa")
def test(a: str = "a", b: int = 2, c: list[str] = ["a", 'b', 'c']) -> None:
    print(a, b, c)
    pass


def main() -> None:
    test(c=['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])


@app.get("/")
# @middleware  # type: ignore
# @user_is("aaaaaaaaaa")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    main()
