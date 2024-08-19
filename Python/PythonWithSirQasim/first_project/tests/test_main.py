from first_project import main

def test_hello1 ():
    r  = main.print_hello()
    assert r == "Hello, World!"


def test_hello2():
    r = main.print_hello()
    assert isinstance(r,str)


def test_hello():
    r = main.print_hello()
    assert r != "Bye, World!"