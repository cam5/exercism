"""This is a module for use with the hello_world exercise on the python track
of exercism."""


def hello(name=''):
    """Given a a name, greets specifically; otherwise, generically."""

    return 'Hello, World!' if name == "" else "Hello, " + name + "!"
