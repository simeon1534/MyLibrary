from conn import db

class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    books = db.relationship('BookAuthor',backref='author',lazy=True)

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name})>"
