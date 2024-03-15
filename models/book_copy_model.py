from conn import db


class BookCopy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_published = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    isbn = db.Column(db.String(30), nullable=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    cover_base64 = db.Column(db.LargeBinary, nullable=True)

    def __repr__(self):
        return f"<BookCopy(id={self.id}, year_published={self.year_published}, book_id={self.book_id}, isbn={self.isbn}, series_id={self.series_id})>"
