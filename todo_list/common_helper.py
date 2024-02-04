from .models import Task
import json

class CommonHelper():
    @staticmethod
    def serialize(task):
        serialized_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'created_on': task.created_on.isoformat() if task.created_on else None
        }
        return serialized_data
    
    @staticmethod
    def deserialize(data):
        try:
            data_dic = json.loads(data)
        except json.JSONDecodeError:
            return None
        
        if 'title' not in data_dic and 'description' not in data_dic and 'completed' not in data_dic:
            return None
        
        title = data_dic['title']
        description = data_dic['description']
        completed = data_dic['completed']

        return Task(title=title, description=description, completed=completed)
