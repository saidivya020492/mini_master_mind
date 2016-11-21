import random
from InputHandler import *
from SecretCode import *
from utils import *
import getpass


class Game:

    def __init__(self):
        self.secret_code=None
        self.previous_input=[]

    def start(self):
        attempts = 0
        self.secret_code=self.read_secret_code()
        while attempts < 6:
            input = self.read_input()
            attempt_res,msg ,attempt_suggestion= self.tally_with_secret_code(input)
            if  attempt_res is  True:
                print msg
                exit(0)
            else:

               attempts +=1
               print "ATTEMPT "+str(attempts)+" score : "+ str (msg)
               print "\n" + attempt_suggestion
        print "!! You Lost ! Please Try AGAIN"


    def read_secret_code(self):
        secret_code = getpass.getpass("Are you a CODER !!! Please enter your SECRET code: ")
        sc_obj = SecretCode()
        secret_code_res, secret_code_err = sc_obj.store_secret_code(secret_code)
        if secret_code_res:
            return sc_obj.secret_code
        else:
            print "!! Try AGAIN"
            exit(1)

    def read_input(self):
        input = raw_input("Please enter your colour code: ")
        inp_obj=InputHandler()
        validate_res,validate_err = inp_obj.store_input_attempt(input)
        if validate_res:
            return inp_obj.input_attemnpt
        else:
            print "!! Try AGAIN"
            exit(1)


    def tally_with_secret_code(self,input):
        """
        Black : If color and position matches
        White : If color only matches
        NoMatches  : If nothing matches
        """
        white = 0
        black = 0
        nomatch = 0
        score_list = []
        suggestion=""
        print "Scoring your color code\n"
        print "Black : If color and position matches\nWhite : If color only matches\nNone  : If nothing matches\n"
        color = 0
        secret_code = self.secret_code
        input_code = list(input)
        for i in range(0,len(input_code)):
            if input_code[i] in secret_code:
                if input_code[i] == secret_code[i]:
                    black+=1
                else:
                    white+=1
            else:
                nomatch+=1
        if black == 4:
            return True, "You won the game!!!",""
        else:
            suggestion=self.get_suggestion(input,[black,white,nomatch])
            self.previous_input.append(input)
            return False, "\nBlacks  : "+str(black)+"\nWhites  : "+str(white)+"\nNoColor : "+str(nomatch),suggestion


    def get_suggestion(self,input,score):
        suggestion=""
        if (not len(self.previous_input) == 0) and input in self.previous_input:
            suggestion += "\nHey !! this combination was already attempted!! in attempt" + str(
                self.previous_input.index(input) + 1)
        """if score[2] > 0:
            missing_colors = set(ValidateCode.valid_list) - set(list(input))
            print missing_colors
            print input
            print ValidateCode.valid_list
            suggestion += "\nYou  can try  from these colors : "+str(list(missing_colors))"""
        if score[1]>1 and score[2] == 0:
            suggestion +="\n!! You are almost there try swapping colors"
        if score[0]==3 and score[2]==1:
            suggestion += "\n!! You Nailed Three Positions try a different color"

        return suggestion





if __name__ == '__main__':
    Game().start()
