def get_data(upper: bool = False) -> str:
    return 'hello'


def make_up(s: str) -> str:
    return s.upper()


result = make_up(get_data())

print(result)


