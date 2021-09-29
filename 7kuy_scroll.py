def get_section_id(scroll, sizes):
    where = 0
    for i in range(len(sizes)):
        where += sizes[i]
        if where > scroll:
            return i
    return -1


print(get_section_id(299, [300, 200, 400, 600, 100]))
print(get_section_id(300, [300, 200, 400, 600, 100]))
print(get_section_id(1600, [300, 200, 400, 600, 100]))
