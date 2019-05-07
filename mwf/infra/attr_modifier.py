def setter(attr, req_type):
    def set_any(self, value):
        nonlocal attr, req_type
        if not isinstance(value, req_type):
            raise ValueError(f"value {value} is not type {req_type}")
        setattr(self, attr, value)

    return set_any


def getter(attr):
    def get_any(self):
        nonlocal attr
        if not hasattr(self, attr):
            raise ValueError(f"attribute {attr} not found")
        return getattr(self, attr)

    return get_any

