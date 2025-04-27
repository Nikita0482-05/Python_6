def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([1, 1]) == 1
assert average_num([2.5, 3.5]) == 3
assert average_num([1, 2, 3, 4, 5]) == 3
assert average_num([1.0, 2.0, 3.0, 4.0, 5.0]) == 3
assert average_num([1, 2.5, 3, 4.5, 5]) == 3.2
assert average_num(['1', '2', '3']) == 2
assert average_num([1, 2, 3, 'a']) == "Bad request"
assert average_num([10, -5, 0, 5]) == 2.5
assert average_num([1000, 2000, 3000]) == 2000