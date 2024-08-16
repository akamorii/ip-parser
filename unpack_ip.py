
def unpack_ip(ip):
    def unpack(data):
        if type(data) == list:
            data = data[0]
        return data
    res = [unpack(n) for n in ip]
    string = ''
    for char in res:
        string += str(char)
    return string