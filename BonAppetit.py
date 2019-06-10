import unittest

def bonAppetit(bill, k, b):
    del bill[k]
    value = sum(bill) //2
    if b- value == 0:
        return "Bon Appetit"
    return (b-value)


class someTests(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual(bonAppetit([3, 10, 2, 9], 1, 12), 5)

    def test2(self):
        self.assertAlmostEqual(bonAppetit([3, 10, 2, 9], 1, 7), "Bon Appetit")

if __name__ == "__main__":
    unittest.main()

