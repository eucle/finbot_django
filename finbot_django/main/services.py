def make_tuple_of_lists(lst: list) -> tuple[list, list]:
    _key_1 = list(lst[0].keys())[0]
    _key_2 = list(lst[0].keys())[1]
    _list_1 = [el[_key_1] for el in lst]
    _list_2 = [float(el[_key_2]) for el in lst]
    return _list_1, _list_2
