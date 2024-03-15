from conn import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.String(255),nullable=True)

    authors = db.relationship('BookAuthor', backref='book', lazy=True)
    book_copies = db.relationship('BookCopy', backref='book', lazy=True)

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, category_id={self.category_id}, description={self.description})>"
