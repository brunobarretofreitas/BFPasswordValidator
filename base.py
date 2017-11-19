import re

__version__ = "1.0.0"

__validators__=['max_length', 'min_length', 'number_required', 'special_characters_required', 'uppercase_required']

def password_validator(**kwargs):
    return PasswordValidator(**kwargs)

class PasswordValidator:
    def __init__(self, **kwargs):
        self.arguments = kwargs
  
    def validate_max_length(self, password, max_length):
        return (len(password) <= max_length)
    
    def validate_min_length(self, password, min_length):
        return (len(password) >= min_length)

    def validate_number_required(self, password, number_required):
        pattern = re.compile(".*[0-9].*")
        return (pattern.match(password) is not None) and number_required

    def validate_special_characters(self, password, special_characters):
        pattern = re.compile(".*[!@#$%&*=+=-_]")
        return (pattern.match(password) is not None) and special_characters

    def validate_uppercase(self, password, uppercase):
        pattern = re.compile(".*[A-Z].*")
        return (pattern.match(password) is not None) and uppercase

    def validate(self, password):
        for argument, value in self.arguments.iteritems():
            if argument in __validators__:
                validate_method = getattr(self, 'validate_' + argument)
                if(not validate_method(password, value)):
                    return False
            else:
                raise InvalidValidator(validator=argument)
        
        return True

class InvalidValidator(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, "Invalid Validator {0}".format(kwargs.get('validator')))