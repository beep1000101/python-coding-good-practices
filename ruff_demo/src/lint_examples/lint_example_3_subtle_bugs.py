def accumulate(x, items=[]):  # mutable default
    items.append(x)
    return items


def shadow_builtins():
    list = [1, 2, 3]  # shadows built-in
    dict = {"a": 1}
    sum = 0
    for i in list:
        sum += i
    return dict


def swallow_exception():
    try:
        risky = 1 / 0
    except Exception:
        pass


def unreachable_branch():
    if False:
        tmp = 123
    return tmp  # tmp may be undefined


def var_scope(flag):
    if flag:
        value = 10
    return value  # value may be undefined
