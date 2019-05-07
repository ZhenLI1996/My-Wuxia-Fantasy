from mwf.infra import getter, setter


class Item:
    def __init__(self,
                 item_id: int,
                 name: str,
                 price: int,
                 desc: str = "an item"):
        self._item_id = item_id
        self._name = name
        self._price = price
        self._desc = desc

    item_id = property(fget=getter("_item_id"))
    name = property(fget=getter("_name"))
    price = property(fget=getter("_price"))
    desc = property(fget=getter("_desc"))
    # name = property(fset=setter("_name", str), fget=getter("_name"))
    # price = property(fset=setter("_price", str), fget=getter("_price"))
    # desc = property(fset=setter("_desc", str), fget=getter("_desc"))

    def __str__(self):
        return f"Item #{self._item_id} {self._name} (\u00a4 {self._price}): {self._desc}"

    def __repr__(self):
        return f"Item(" \
               f"item_id={self._item_id}," \
               f"name={self._name}," \
               f"price={self._price}," \
               f"desc={self._desc}," \
               f")"
