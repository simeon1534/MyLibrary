from conn import db


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    series = db.relationship('Series', backref='publisher', lazy=True)


    def __repr__(self):
        return f"<Publisher(id={self.id}, name={self.name})>"