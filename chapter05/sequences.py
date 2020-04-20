# _*_ coding: utf-8 _*_

"""
(1) python序列类型分类：
    1、容器序列 list tuple deque
    2、扁平序列 str bytes bytearray array.array
    3、可变序列 list deque bytearray array
    3、不可变序列 str tuple bytes
(2) collections --> abc --> __all__
    __all__ = ["Awaitable", "Coroutine",
           "AsyncIterable", "AsyncIterator", "AsyncGenerator",
           "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
           "Sized", "Container", "Callable", "Collection",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence"(不可变), "MutableSequence"(可变),
           "ByteString",
           ]
"""

from collections import abc

"""
+ and  +=
------------
+= --> abc --> MutableSequence.iadd --> extend --> append
以上就解释为什么 += 能够实现extend方法的效果
----------
MutableSequence.iadd
def __iadd__(self, values):
    self.extend(values)
    return self
    
extend 是通过append方法对可迭代序列进行遍历逐一添加，所以解释了extend能够拆开容器，逐一添加
def extend(self, iterable: Iterable[_T]) -> None
L.extend(iterable) -> None -- extend list by appending elements from the iterable

append 追加的是一个对象，所以其能够添加到一个完整的序列结构，不是拆开序列结构
L.append(object) -> None -- append object to end
"""

a = [1, 2]
c = a + [3, 4]  # + 两边必须是类型相同的序列，不然会报错

# += 是“就地”改变
a += (3, 4)  # 这个为什么能够就地加，而且能够加不一样的序列
a.extend((3, 4))
a.append((5, 6))
print(a)


"""
切片不会修改遇原序列，而是重新创建一个序列并返回
"""
