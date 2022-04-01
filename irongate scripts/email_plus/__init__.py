import re


class Email:

    def check_email(self, email):
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if (re.search(regex, email)):   #return true if it is in email format
            return True
        else:
            return False
           
