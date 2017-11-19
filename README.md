# BFPasswordValidator
> Simple password validator for python projects

## Features

- [x] Uppercase verification (At least one Uppercase letter required, True or False)
- [x] Numbers verification (At least one number required, True or False)
- [x] Special Characters verification (At least one Special Character required, True or False)
- [x] Max and Min length of passwords

## Options
* ``` max_length ``` : Password maximum length : Integer
* ``` min_length ``` : Password minimum length : Integer
* ``` special_characters_required ``` : Password requires at least one special character : Boolean
* ``` number_required ``` : Password requires at least one number : Boolean
* ``` uppercase_required ``` : Password requires at least one uppercase letter : Boolean

## Usage
```python
from bfpasswordvalidator import password_validator
validator = password_validator(options)
validator.validate(password)
```

## Example

```python
from bfpasswordvalidator import password_validator

def is_password_valid(password):
    validator = password_validator(max_length=30, min_length=8, number_required=True)
    return validator.validate(password)
```
## Contribute
Feel yourself free to contribute to this project, fork it and code :)

## Meta

Bruno B. Freitas – brunobarretofreitas@outlook.com

[https://github.com/brunobarretofreitas/BFPasswordValidator/](https://github.com/brunobarretofreitas/BFPasswordValidator)
