import unittest

from markdown_generator import generate_documentation


class TestMarkdownGenerator(unittest.TestCase):

    def test_functions_and_classes(self):
        source = '''"""Example module documentation."""

def hello():
    """Say hello."""
    return "hello"

class Greeter:
    """A greeting class."""
    pass
'''
        result = generate_documentation(source, "example")

        self.assertIn("# example", result)
        self.assertIn("hello", result)
        self.assertIn("Greeter", result)
        self.assertIn("Say hello.", result)

    def test_invalid_source(self):
        with self.assertRaises(SyntaxError):
            generate_documentation("def broken(", "bad")


if __name__ == "__main__":
    unittest.main()
