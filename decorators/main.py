def uppercase_decorator(function):
    def wrapper():
        result = function() # say_hi()
        make_uppercase = result.upper()
        return make_uppercase

    return wrapper


def make_list(f):
    def wrapper():
        result = f()
        return result.split(' ')
    return wrapper


@make_list
def say_hi():
    return 'hello there'

result = say_hi()

print(result)



