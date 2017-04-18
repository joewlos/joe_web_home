from shared import db

# Create our database model
class Articles(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    article_type = db.Column(db.String(120))
    article_text = db.Column(db.Text)

    def __init__(self, email):
        self.article_text = article_text
        self.article_type = article_type

    def __repr__(self):
        return '<article_text %r>' % self.article_text
