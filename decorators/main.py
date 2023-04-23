def uppercase_decorator(function):
    def wrapper():
        result = function() # say_hi()
        upper_list = []
        for item in result:
            upper_list.append(item.upper())
        return upper_list

    return wrapper


def make_list(f):
    def wrapper():
        result = f()
        return result.split(' ')
    return wrapper


@uppercase_decorator
@make_list
def say_hi():
    return 'hello there'

result = say_hi()

print(result)



