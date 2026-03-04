# This file defines what a User is

class Person:
    """Base class for all people in the system"""
    _id_counter = 1000
    
    def __init__(self, name):
        self._name = name
        self.id = Person._id_counter
        Person._id_counter += 1
    
    @property
    def name(self):
        """Get the person's name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the person's name with validation"""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()


class User(Person):
    """Represents a user in the project management system"""
    def __init__(self, name, email):
        super().__init__(name)
        self._email = email
    
    @property
    def email(self):
        """Get the user's email"""
        return self._email
    
    @email.setter
    def email(self, value):
        """Set the user's email with validation"""
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Email must be a valid email address")
        self._email = value.strip()
    
    def __str__(self):
        """User string representation for CLI output"""
        return f"{self.name} ({self.email})"
    
    def __repr__(self):
        """User official representation"""
        return f"User(name='{self.name}', email='{self.email}', id={self.id})"
    
    # Convert user to dictionary (for saving to JSON)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }