datas = [
    ['hello', '2', 'world', ':-)'],
    ['1234', '1567', '-2', 'computer science'],
    ['Russia', 'Denmark', 'Kazan'],
]


def get_less_then_4_character_from_list(inp_list):
    return [el for el in inp_list if len(el) < 4]


for data in datas:
    print(get_less_then_4_character_from_list(data))



