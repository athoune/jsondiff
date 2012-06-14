

def to_collection(data):
    return _handle(data, set(), None)

#[TODO] def from_collection(values)

#[TODO] def diff(data1, data2)
# key starting with - are removed

#[TODO] def patch(patch, data)


def append_path(path, slug):
    if path == None:
        return slug
    return "%s.%s" % (path, slug)


def _handle(data, values, path):
    if 'items' in dir(data):
        for k, v in data.items():
            values = _handle(v, values, append_path(path, k))
        return values
    if '__iter__' in dir(data):
        for i, v in enumerate(data):
            values = _handle(v, values, "%s[%i]" % (path, i))
        return values
    values.add((path, data))
    return values
