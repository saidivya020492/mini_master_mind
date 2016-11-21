from utils import *

class SecretCode:

    def __init__(self):
        self.secret_code=None

    def store_secret_code(self,code):
        #code = raw_input('Enter the secret code:')
        res,err_msg= ValidateCode().validate(code)
        if not err_msg == "":
            print ""+err_msg
        if res:
            self.secret_code = code
            print "Secret Code Stored"
            return True,err_msg
        else:
            return False,err_msg



