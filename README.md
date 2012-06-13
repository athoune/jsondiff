JsonDiff
========

Transforma json like data in a set of key/value.

Works with json like data, it should works with [msgpack](http://msgpack.org/)
or [bson](http://bsonspec.org/) or even [tnetstrings](http://tnetstrings.org/).

Exemple
-------

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

You can now diff to json like data.

Licence
-------

MIT © Mathieu Lecarme 2012

