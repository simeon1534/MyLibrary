
from conn import db
class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book',backref='category',lazy=True)

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"
