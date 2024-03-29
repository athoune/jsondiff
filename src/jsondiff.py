

def to_collection(data):
    return _handle(data, set(), None)

#[TODO] def from_collection(values)


def diff(data1, data2):
    d1 = to_collection(data1)
    d2 = to_collection(data2)
    keys = set()
    removing = {}
    for k, v in d1 - d2:
        removing[k] = v
        keys.add(k)
    adding = {}
    for k, v in d2 - d1:
        adding[k] = v
        keys.add(k)
    diff = {}
    for k in keys:
        if k in removing and k in adding:
            print "modifying", k
            diff[k] = adding[k]
            continue
        if k in adding:
            diff["+%s" % k] = adding[k]
            continue
        diff["-%s" % k] = removing[k]
    return diff

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
