# This file handles all the file operations (saving to JSON)

import json
import os

class Storage:
    def __init__(self, filename='data/storage.json'):
        self.filename = filename
        # Create data folder if it doesn't exist
        os.makedirs('data', exist_ok=True)
        # Load existing data or create new
        self.data = self.load()
    
    # Load data from JSON file
    def load(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    content = f.read().strip()
                    if not content:
                        return self._create_empty_data()
                    return json.loads(content)
            return self._create_empty_data()
        except (json.JSONDecodeError, IOError) as e:
            # If file is malformed, return empty structure
            print(f" Warning: Could not load data ({str(e)}). Starting fresh.")
            return self._create_empty_data()
    
    @staticmethod
    def _create_empty_data():
        """Create empty data structure"""
        return {'users': [], 'projects': [], 'tasks': []}
    
    # Save data to JSON file
    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f" Error saving data: {str(e)}")
    
    # ----- USER METHODS -----
    def add_user(self, user_dict):
        self.data['users'].append(user_dict)
        self.save()
    
    def get_users(self):
        """Get all users as list"""
        return self.data['users']
    
    @classmethod
    def get_all_users(cls, filename='data/storage.json'):
        """Class method to retrieve all users from storage"""
        storage = cls(filename)
        return storage.get_users()
    
    def find_user(self, email):
        for user in self.data['users']:
            if user['email'] == email:
                return user
        return None
    
    # ----- PROJECT METHODS -----
    def add_project(self, project_dict):
        self.data['projects'].append(project_dict)
        self.save()
    
    def get_projects(self):
        """Get all projects as list"""
        return self.data['projects']
    
    @classmethod
    def get_all_projects(cls, filename='data/storage.json'):
        """Class method to retrieve all projects from storage"""
        storage = cls(filename)
        return storage.get_projects()
    
    def find_project(self, title):
        for project in self.data['projects']:
            if project['title'] == title:
                return project
        return None
    
    # ----- TASK METHODS -----
    def add_task(self, task_dict):
        self.data['tasks'].append(task_dict)
        self.save()
    
    def get_tasks(self):
        """Get all tasks as list"""
        return self.data['tasks']
    
    @classmethod
    def get_all_tasks(cls, filename='data/storage.json'):
        """Class method to retrieve all tasks from storage"""
        storage = cls(filename)
        return storage.get_tasks()
    
    def complete_task(self, title):
        for task in self.data['tasks']:
            if task['title'] == title:
                task['status'] = 'completed'
                self.save()
                return True
        return False