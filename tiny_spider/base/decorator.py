import functools


def singleton(cls):
    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kwargs):
        """
            if '__it__' exists, it implies that object has been created.
            And the value of '__it__' is the very object that created first.
        :param cls: the class
        :param args:
        :param kwargs:
        :return:
        """
        it = cls.__dict__.get('__it__')
        if it is not None:
            return it

        cls.__it__ = it = cls.__new_original__(cls, *args, **kwargs)

        it.__init_original__(*args, **kwargs)
        return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__
    return cls
