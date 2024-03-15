from conn import db

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)

    book_copies = db.relationship('BookCopy',backref='series',lazy=True)

    def __repr__(self):
        return f"<Series(id={self.id}, name={self.name}, publisher_id={self.publisher_id})>"