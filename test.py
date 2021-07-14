import unittest

from Balance import Loan


class SimpleTest(unittest.TestCase):
    

    def test_balance(self):
        loan_obj = Loan(
            "IDIDI",
            "Dale",
            10000,
            5,
            4
        )
        balance = loan_obj.balance(5)
        self.assertEqual(balance.get("amount_paid"), 1000)
        self.assertEqual(balance.get("no_Of_Emis_Left"), 55)

    
    def test_balance_with_payment(self):
        loan_obj = Loan(
            "UON",
            "Shelly",
            15000,
            2,
            9   
        )
        loan_obj.payment(7000, 12)
        balance = loan_obj.balance(12)
        self.assertEqual(balance.get("amount_paid"), 15856)
        self.assertEqual(balance.get("no_Of_Emis_Left"), 3)


if __name__ == '__main__':
    unittest.main()