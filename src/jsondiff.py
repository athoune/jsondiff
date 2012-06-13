

def to_list(data):
    _data, values, _path = _handle(data, set(), None)
    return values


def append_path(path, slug):
    if path == None:
        return slug
    return "%s.%s" % (path, slug)


def _handle(data, values, path):
    if 'items' in dir(data):
        for k, v in data.items():
            _, values, _ = _handle(v, values, append_path(path, k))
        return None, values, None
    if '__iter__' in dir(data):
        for i, v in enumerate(data):
            _, values, _ = _handle(v, values, "%s[%i]" % (path, i))
        return None, values, None
    values.add((path, data))
    return data, values, path

if __name__ == '__main__':
    data = {"age": 42,
            "name": "Robert",
            "tags": ["pim", "pam", "poum"],
            "like": {
                "food": "ramen"
                }
            }
    print data
    print to_list(data)
