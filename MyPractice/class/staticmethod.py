import re

class Username:
    def __init__(self, name: str):
        if not self.is_valid_username(name):
            raise ValueError("Invalid username")       
        self.name = name
        
    @staticmethod
    def is_valid_username(name):
        return re.match(r"^[a-zA-Z0-9]{3,20}$", name) is not None