from utils import *

class InputHandler:

    def __init__(self):
        self.input_attemnpt=None

    def store_input_attempt(self,input_attempt):
        res, err_msg = ValidateCode().validate(input_attempt)
        if not err_msg == "":
            print "" + err_msg
        if res:
            self.input_attemnpt = input_attempt
            return True, err_msg
        else:
            return False, err_msg

