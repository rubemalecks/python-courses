def validate_type(type):
    def validate(func):
        def inner(*args, **kwargs):
            if all(isinstance(val, type) for val in args):
                return func(*args)

        return inner

    return validate


@validate_type(int)
def soma(x, y):
    return x + y


print(soma(1, 1))
