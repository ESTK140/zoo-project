import unittest
from zoo import get_ticket_price  # Import the function

class TestZooTicketPrice(unittest.TestCase):
    def test_invalid_age(self):
        # C1b1: age < 0
        with self.assertRaises(ValueError):
            get_ticket_price(-1)

    def test_child_price(self):
        # C1b2: 0 ≤ age ≤ 12
        self.assertEqual(get_ticket_price(0), 50)
        self.assertEqual(get_ticket_price(12), 50)

    def test_teen_price(self):
        # C1b3: 13 ≤ age ≤ 20
        self.assertEqual(get_ticket_price(13), 100)
        self.assertEqual(get_ticket_price(20), 100)

    def test_adult_price(self):
        # C1b4: 21 ≤ age ≤ 60
        self.assertEqual(get_ticket_price(21), 150)
        self.assertEqual(get_ticket_price(60), 150)

    def test_senior_price(self):
        # C1b5: age > 60
        self.assertEqual(get_ticket_price(61), 100)

if __name__ == "__main__":
    unittest.main()
