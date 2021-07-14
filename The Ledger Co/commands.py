import sys
import cmd

from Balance import Loan
from logger import logger


class LedgerCoShell(cmd.Cmd):

    intro = 'Welcome to LedgerCo Emi Calculator.   Type help or ?  to\
 list commands.\n'
    prompt = '(The ledger Co) '
    bank = {}

    # ----- basic The Ledger Co commands -----


    def do_LOAN(self, arg):

        # Command Format: LOAN Bankname Username Principal_amount No_of_years Rate_of_interst
        try:
            arg_list = parse(arg)
            bankname = arg_list[0]
            name = arg_list[1]
            principal_amount = int(arg_list[2])
            no_Of_years = int(arg_list[3])
            rate = int(arg_list[4])
        except:
            logger.warning("Please check the input format")

        obj_name = (bankname+"_"+name).upper()
        self.bank[obj_name] = Loan(
            bankname, name, principal_amount, no_Of_years, rate)


    def do_BALANCE(self, arg):
        # Command Format: BALANCE Bankname Username Emi_number
        try:
            arg_list = parse(arg)
            bankname = arg_list[0]
            name = arg_list[1]
            emi_number = int(arg_list[2])
        except:
            logger.warning("Please check the input format")

        obj_name = (bankname+"_"+name).upper()
        if obj_name in self.bank:
            response = self.bank[obj_name].balance(emi_number)
            print(response['bankname']
                  + ' '+response['person']
                    + ' '+str(response['amount_paid'])
                    + ' '+str(response['no_Of_Emis_Left'])
                  )
        else:
            logger.warning("User Not Found")


    def do_PAYMENT(self, arg):
        # Command Format: PAYMENT Bankname Username LumpsumAmount Eminumber
        try:
            arg_list = parse(arg)
            bankname = arg_list[0]
            name = arg_list[1]
            lump_sum = int(arg_list[2])
            emi_number = int(arg_list[3])
            obj_name = (bankname+"_"+name).upper()
        except:
            logger.warning("Please check the input format")
        obj_name = (bankname+"_"+name).upper()
        if obj_name in self.bank:
            self.bank[obj_name].payment(lump_sum, emi_number)
        else:
            logger.warning("User Not Found")


    def do_exit(self, arg):
        'Exit from the Shell'
        print('Exiting...')
        return True


def parse(arg):
    # Convert a series of zero or more numbers to an argument tuple
    return tuple(map(str, arg.split()))