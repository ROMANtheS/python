def make_accumulator(stop_value):
    collection = []
    
    def accumulator(value):
        nonlocal collection
        if value == stop_value:
            result = collection.copy()
            collection.clear()
            return result
        collection.append(value)
        return None
    
    return accumulator
def validate(*validators):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, validator in zip(args, validators):
                if not validator(arg):
                    raise ValueError(f"Validation failed for argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@validate(lambda x: isinstance(x, (int, float)), lambda x: x is not None)
def make_validated_accumulator(stop_value):
    collection = []
    
    def accumulator(value):
        nonlocal collection
        if value == stop_value:
            result = collection.copy()
            collection.clear()
            return result
        collection.append(value)
        return None
    
    return accumulator