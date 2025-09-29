from datetime import datetime

class CategoryEvent:
    def __init__(self, category_id, timestamp=None):
        self.category_id = category_id
        self.timestamp = timestamp or datetime.utcnow()

class CategoryCreated(CategoryEvent):
    def __init__(self, category_id, timestamp, data):
        super().__init__(category_id, timestamp)
        self.data = data

    def __repr__(self):
        return f"<CategoryCreated id={self.category_id} at={self.timestamp}>"

class CategoryUpdated(CategoryEvent):
    def __init__(self, category_id, timestamp, updated_fields):
        super().__init__(category_id, timestamp)
        self.updated_fields = updated_fields

    def __repr__(self):
        return f"<CategoryUpdated id={self.category_id} fields={self.updated_fields} at={self.timestamp}>"

class CategoryActivated(CategoryEvent):
    def __repr__(self):
        return f"<CategoryActivated id={self.category_id} at={self.timestamp}>"

class CategoryDeactivated(CategoryEvent):
    def __repr__(self):
        return f"<CategoryDeactivated id={self.category_id} at={self.timestamp}>"
