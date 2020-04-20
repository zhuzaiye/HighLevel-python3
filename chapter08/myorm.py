# _*_ coding: utf-8 _*_

"""
元类编程
"""
import numbers


class Field:
    pass


class IntField:
    # 数据描述
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.da_column = db_column
        if min_value is not None:
            if isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller tha max_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")

        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")

        self._value = value


class CharField:
    def __init__(self, da_column, max_length=None):
        self.value = None
        self.max_length = max_length
        self.da_column = da_column
        if max_length is None:
            raise ValueError("you must specify max_length for charfield")

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self.value = value


class ModelMeteClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fileds = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                Field[key] = value

        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fileds
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMeteClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super.__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fileds.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))
        sql = "insert {db_table}({fields}) value({values})".format(self._meta["db_fields"], fields=",".join(fields),
                                                                   values=",".join(values))

        # 查看django的model


class User(BaseModel):
    name = CharField(da_column="", max_length=10)
    age = IntField(db_column="", min_value=0, max_value=100)

    class Meta:
        db_table = "user"


if __name__ == '__main__':
    user = User()
    user.anem = "bobby"
    user.age = 28
