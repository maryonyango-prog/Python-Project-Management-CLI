# This file defines what a Project is

class Project:
    """Represents a project owned by a user"""
    _id_counter = 2000
    
    def __init__(self, title, user_email):
        self._title = title
        self.user_email = user_email
        self.id = Project._id_counter
        Project._id_counter += 1
    
    @property
    def title(self):
        """Get the project title"""
        return self._title
    
    @title.setter
    def title(self, value):
        """Set the project title with validation"""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()
    
    def __str__(self):
        """Project string representation for CLI output"""
        return f"{self.title} (Owner: {self.user_email})"
    
    def __repr__(self):
        """Project official representation"""
        return f"Project(title='{self.title}', user_email='{self.user_email}', id={self.id})"
    
    # Convert project to dictionary (for saving to JSON)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user_email': self.user_email
        }