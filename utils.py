
class ValidateCode:

    valid_list = ["P", "B", "G", "Y", "R", "O"]

    def validate(self,code):
        code_list = list(code)
        if not len(code_list) == 4:
            return False,"INPUT Should be of length 4 !!"
        elif self.check_colors(code_list)[0]== False:
             return False,"INVALID color Selected : "+str(self.check_colors(code_list)[1])+"\n !! Pls Select from  : "+str(self.valid_list)
        elif self.check_duplicates(code_list)[0]==False:
            return False,"INPUT contains Dulpicate colors : " + str(self.check_duplicates(code_list)[1])
        else:
            return True,""

    def check_duplicates(self,code_list):
        dups = [element for index, element in enumerate(code_list) if code_list.count(element) > 1]
        if not len(dups) == 0:
            no_duplicates = set(dups)
            return False,(list(no_duplicates))
        return True,""

    def check_colors(self,code_list):
        for color in code_list:
            if not color in self.valid_list:
                return False,color
        return True,""