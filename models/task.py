# This file defines what a Task is

class Task:
    """Represents a task within a project"""
    _id_counter = 3000
    
    def __init__(self, title, project_title, assigned_to):
        self._title = title
        self.project_title = project_title
        self.assigned_to = assigned_to
        self._status = 'pending'  # pending or completed
        self.id = Task._id_counter
        Task._id_counter += 1
    
    @property
    def title(self):
        """Get the task title"""
        return self._title
    
    @title.setter
    def title(self, value):
        """Set the task title with validation"""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()
    
    @property
    def status(self):
        """Get the task status"""
        return self._status
    
    @status.setter
    def status(self, value):
        """Set the task status with validation"""
        if value not in ('pending', 'completed'):
            raise ValueError("Status must be 'pending' or 'completed'")
        self._status = value
    
    def __str__(self):
        """Task string representation for CLI output"""
        status_icon = "✅" if self.status == 'completed' else "⏳"
        return f"{status_icon} {self.title} ({self.project_title})"
    
    def __repr__(self):
        """Task official representation"""
        return f"Task(title='{self.title}', project='{self.project_title}', assigned_to='{self.assigned_to}', status='{self.status}', id={self.id})"
    
    # Convert task to dictionary (for saving to JSON)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'project_title': self.project_title,
            'assigned_to': self.assigned_to,
            'status': self.status
        }