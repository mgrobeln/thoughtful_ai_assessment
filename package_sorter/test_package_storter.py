import unittest
from package_sorter.__main__ import get_volume, sort

class TestPackageSorter(unittest.TestCase):
    def test_get_volume(self):
        """Test the calculation of volume."""
        self.assertEqual(get_volume(2, 3, 4), 24)
        self.assertEqual(get_volume(1.5, 2.5, 3.5), 13.125)
        self.assertEqual(get_volume(0, 5, 10), 0)

    def test_sort_standard(self):
        """Test that packages are classified as STANDARD when not bulky or heavy."""
        self.assertEqual(sort(width=10, height=10, length=10, mass=5), "STANDARD")
        self.assertEqual(sort(width=50, height=50, length=50, mass=10), "STANDARD")

    def test_sort_bulky(self):
        """Test that packages are classified as SPECIAL when bulky."""
        self.assertEqual(sort(width=200, height=10, length=10, mass=5), "SPECIAL")
        self.assertEqual(sort(width=10, height=10, length=200, mass=5), "SPECIAL")
        self.assertEqual(sort(width=10, height=10, length=10, mass=5), "STANDARD")
        self.assertEqual(sort(width=10, height=200, length=10, mass=5), "SPECIAL")
        self.assertEqual(sort(width=10, height=10, length=10, mass=5), "STANDARD")



    def test_sort_heavy(self):
        """Test that packages are classified as SPECIAL when heavy."""
        self.assertEqual(sort(width=10, height=10, length=10, mass=25), "SPECIAL")
        self.assertEqual(sort(width=99, height=100, length=100, mass=20), "SPECIAL")

    def test_sort_rejected(self):
        """Test that packages are classified as REJECTED when both bulky and heavy."""
        self.assertEqual(sort(width=200, height=200, length=200, mass=25), "REJECTED")
        self.assertEqual(sort(width=150, height=150, length=150, mass=30), "REJECTED")

    def test_sort_invalid_input(self):
        """Test that invalid inputs raise a ValueError."""
        with self.assertRaises(ValueError):
            sort(width="abc", height=10, length=10, mass=5)
        with self.assertRaises(ValueError):
            sort(width=10, height="xyz", length=10, mass=5)
        with self.assertRaises(ValueError):
            sort(width=10, height=10, length="foo", mass=5)
        with self.assertRaises(ValueError):
            sort(width=10, height=10, length=10, mass="bar")

if __name__ == "__main__":
    unittest.main()
