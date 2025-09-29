import uuid
from datetime import datetime
from events.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated,
)

class Category:
    def __init__(self, name, description="", is_active=True, id=None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.description = description
        self.is_active = is_active
        self.events = []
        self._validate()
        self._register_event(CategoryCreated(self.id, datetime.utcnow(), self.to_dict()))

    def _validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Name must be a non-empty string")

    def update(self, name=None, description=None):
        updated_fields = {}
        if name is not None and name != self.name:
            self.name = name
            updated_fields['name'] = name
        if description is not None and description != self.description:
            self.description = description
            updated_fields['description'] = description
        if updated_fields:
            self._register_event(CategoryUpdated(self.id, datetime.utcnow(), updated_fields))

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self._register_event(CategoryActivated(self.id, datetime.utcnow()))

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self._register_event(CategoryDeactivated(self.id, datetime.utcnow()))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active,
            "class_name": self.__class__.__name__
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description", ""),
            is_active=data.get("is_active", True)
        )

    def _register_event(self, event):
        self.events.append(event)