# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
import re

class PasswordManager2():
    def __init__(self):
        self.allPasswords = {}



    def is_valid(self, password):
        characters = "!@$%&"

        justPasswords = [data[0] for data in self.allPasswords.values()]
        if password in justPasswords:
            return False
        elif len(password)>7:
            if re.search(f"[{re.escape(characters)}]", password):
                return True
        return False
    
    def add(self, service, password):
        if self.is_valid(password):
            self.allPasswords[service] = [password, datetime.now()]

    def remove(self, service):
        self.allPasswords.pop(service)

    def update(self, service, password):
        self.add(service, password)


    def get_for_service(self, service):
        if service in self.list_services():
            return self.allPasswords[service][0]

    def list_services(self):
        return list(self.allPasswords.keys())
    
    def sort_services_by(self, sort, reverse = None):
        if sort == "service":
            sortedServices = sorted(self.allPasswords.keys())
        elif sort == "added_on":
            sortedList = sorted(self.allPasswords.items(), key = lambda password:password[1][1])
            sortedServices = [x[0] for x in sortedList]

        if reverse != None:
            return sortedServices[::-1]
        return sortedServices




