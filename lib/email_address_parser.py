# your code goes here!
import re

class EmailAdresssParser:
    def __init__(self, addresses):
        self.addresses = addresses
        
    def parse(self):
        emails =re.split(r'[,\s]+', self.addresses.strip())
        unique_mails = sorted(set(emails))
        return unique_mails
    
emails = "john@doe.com, person@somewhere.org john@doe.com"
parses = EmailAdresssParser(emails)

print(parses.parse())