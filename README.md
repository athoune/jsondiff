JsonDiff
========

Transforma json like data in a set of key/value.

Works with json like data, it should works with [msgpack](http://msgpack.org/)
or [bson](http://bsonspec.org/) or even [tnetstrings](http://tnetstrings.org/).

Exemple
-------

### Normalisation

    {'age': 42,
    'like': {
        'food': 'ramen'},
    'name': 'Robert',
    'tags': ['pim', 'pam', 'poum']}

Will be transformed to

    set([
        ('name', 'Robert'),
        ('age', 42),
        ('tags[2]', 'poum'),
        ('tags[1]', 'pam'),
        ('like.food', 'ramen'),
        ('tags[0]', 'pim')])

### Diff

    data1 = {"age": 42,
            "name": "Bob",
            "food": "okonomiyaki"
            }
    data2 = {"name": "Casimir",
            "Location": "Torcy",
            "age": 42
            }
    assert diff(data1, data2) == {
        '-food': 'okonomiyaki',
        'name': 'Casimir',
        '+Location': 'Torcy'}

Key are unique, patch don't have to remove and add data.

Licence
-------

MIT © Mathieu Lecarme 2012

