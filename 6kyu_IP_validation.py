def is_valid_ip(strng):
    def is_ip_range(x):
        if x.isdigit():
            parsed_num = int(x)
            return str(parsed_num) == x and 0 <= parsed_num <= 255
        return False

    return len(list(filter(lambda x: is_ip_range(x), strng.split(".")))) == 4
