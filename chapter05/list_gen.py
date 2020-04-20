# _*_ coding: utf-8 _*_

"""
列表生成式
生成器
"""


def handle_item(item):
    return item * item


if __name__ == '__main__':
    #
    odd_list = [i for i in range(21) if i % 2 == 1]

    # 更加复杂逻辑
    odd_square = [handle_item(i) for i in range(21) if i % 2 == 1]

    print(type(odd_list))  # <class 'list'>
    print(odd_list)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # --------------------------
    # 生成器表达式
    mean_list = (i for i in range(21) if i % 2 == 0)
    print(type(mean_list))  # <class 'generator'>
    print(mean_list)  # <generator object <genexpr> at 0x00000109220C48E0>

    # -------
    # 字典推导式
    my_dict = {"ZhangFei": "black", "GuanYU": "rea"}
    revert_dict = {value: key for key, value in my_dict.items()}
    print(type(revert_dict))  # <class 'dict'>
    print(revert_dict)  # {'black': 'ZhangFei', 'rea': 'GuanYU'}

    # 集合推导
    my_set = {key for key, value in my_dict.items()}
    print(type(my_set))  # <class 'set'>
    print(my_set)  # {'ZhangFei', 'GuanYU'}
