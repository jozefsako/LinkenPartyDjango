def hello(name):
    return 'Hello ' + 'name'

def test_hello():
    assert hello('name') == 'Hello name'