from jsondiff import to_collection, diff


def test_collection():
    data = {"age": 42,
            "name": "Robert",
            "tags": ["pim", "pam", "poum"],
            "like": {
                "food": "ramen"
                }
            }
    assert to_collection(data) == set([
        ('name', 'Robert'),
        ('age', 42),
        ('tags[2]', 'poum'),
        ('tags[1]', 'pam'),
        ('like.food', 'ramen'),
        ('tags[0]', 'pim')])


def test_diff():
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
