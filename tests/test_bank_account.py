import os
import datetime
import unittest
from unittest.mock import patch
from src.bank_account import BankAccount
from src.exceptions import WithdrawalTimeRestrictionError

class BankAccountTests(unittest.TestCase):

    def setUp(self):   # se ejecuta antes de una prueba
        # lo usamos para inicializar una variable que necesitemos reutilizar
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self):
        # Tear Down se ejecuta cada vez que se acaba una prueba
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def test_deposit(self):
        # account = BankAccount(balance = 1000)
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        # account = BankAccount(balance = 1000)
        new_balance = self.account.withdraw(500)
        # assert new_balance == 500
        self.assertEqual(new_balance, 500, "El balance no es igual")

    def test_get_balance(self):
        # account = BankAccount(balance = 1000)
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())

    def test_transaction_log(self):
        self.account.deposit(500)
        # assert os.path.exists(self.account.log_file)
        self.assertTrue(os.path.exists(self.account.log_file))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    
    def test_deposit_multiple_ammounts(self):
        test_cases = [
            {'amount': 100, "expected": 1100},
            {'amount': 2000, "expected": 3000},
            {'amount': 3000, "expected": 4000},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="Transactions_deposit.txt")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])


if __name__ == '__main__':
    unittest.main()
