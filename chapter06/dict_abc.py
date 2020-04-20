# _*_ coding: utf-8 _*_

"""
"Mapping", "MutableMapping"
---------------------------
A MutableMapping is a generic container for associating
key/value pairs.
This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.
-------------------------
Method -->
1. D.clear() -> None.  Remove all items from D.
2. D.copy() -> a shallow copy of D
3. staticmethod- fromkeys Returns a new dict with keys from iterable and values equal to value.
4. D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
5. D.items() -> a set-like object providing a view on D's items
6. D.keys() -> a set-like object providing a view on D's keys
7. D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised
8. D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.
9. D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
10. D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
"""

from collections import Mapping, MutableMapping

if __name__ == '__main__':
    d = dict()
    print(isinstance(d, MutableMapping))  # True

    default_dict = d.setdefault("ZhangFei", "black")
    print(default_dict)  # black
    print(d)  # {'ZhangFei': 'black'}
    d.update((("GuanYU", "red"),))  # {'ZhangFei': 'black', 'GuanYU': 'red'}
    print(d)
