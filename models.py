import uuid
from datetime import datetime

class Transaction:
    """Represents an individual financial transaction (Income or Expense)."""
    
    TYPES = ["Expense", "Income"]

    def __init__(self, amount, category, description, trans_type="Expense", date=None, trans_id=None):
        self.id = trans_id if trans_id else str(uuid.uuid4())[:8]
        self.trans_type = trans_type if trans_type in self.TYPES else "Expense"
        self.amount = float(amount)
        self.category = category.strip().title()
        self.description = description.strip()
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "id": self.id,
            "trans_type": self.trans_type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data['amount'],
            category=data['category'],
            description=data['description'],
            trans_type=data.get('trans_type', 'Expense'),
            date=data['date'],
            trans_id=data['id']
        )


class UserSettings:
    """Holds configuration parameters like daily expense limit."""
    
    def __init__(self, daily_limit=0.0):
        self.daily_limit = float(daily_limit)

    def to_dict(self):
        return {"daily_limit": self.daily_limit}

    @classmethod
    def from_dict(cls, data):
        return cls(daily_limit=data.get("daily_limit", 0.0))