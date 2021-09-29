def remove_duplicate_ids(obj):
    store_keys = []
    appeared = []
    for key, value in obj.items():
        store_keys.append(int(key))
    store_keys = [x for x in reversed([x for x in sorted(store_keys)])]
    for i in range(len(store_keys)):
        j = 0
        while j < len(obj[str(store_keys[i])]):
            element = obj[str(store_keys[i])][j]
            if element not in appeared:
                appeared.append(element)
                j += 1
            else:
                obj[str(store_keys[i])].pop(j)
    return obj
