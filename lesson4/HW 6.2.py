def gen2():
    list = [1, 107, None, "this_list"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 10):
        print(el)


gen2()
