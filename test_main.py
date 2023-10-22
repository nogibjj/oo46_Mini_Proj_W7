"""
Test the database connection by fetching and displaying results
"""
from assignment_app.assignment import show

import unittest


# test the data
class TestMain(unittest.TestCase):
    def test_conn(self):
        # assert if the connection was successful
        self.assertEqual("Success!", show())


if __name__ == "__main__":
    unittest.main()
