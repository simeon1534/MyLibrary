from conn import db


class BookAuthor(db.Model):
    __tablename__ = 'book_author'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f"<Book(id={self.book_id}, Author(id={self.author_id})>"


