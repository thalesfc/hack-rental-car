def istype_or_error(var, wanted_type, error_msg):
    if not isinstance(var, wanted_type):
        raise TypeError(error_msg)


class Data:
    def __str__(self):
        return '@%s : #%s -> %s' % (self.brand,  self.category, self.price)

    brand = None
    category = None
    price = None
