class UserCheck:
    def __init__(self, approval_required):
        if approval_required == True:
            self.approved = False
        else:
            self.approved = True

    def approval(self, what_to_check=""):
        assert isinstance(what_to_check, str)
        
        if self.approved == True:
            return True

        else:

            print "The program will:\n" + what_to_check

            user_answer = None

            while user_answer == None:

                user_input = raw_input("Type 1 to continue, 0 to stop: ")

                try:
                    user_input = int(user_input)
                    if user_input > 1:
                        user_answer = None
                    else:
                        user_answer = user_input

                except:
                    pass
            
            if user_answer == 1:
                self.approved = True
                return True
            else:
                return False
        
    