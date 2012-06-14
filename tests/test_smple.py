from jsondiff import to_collection


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
