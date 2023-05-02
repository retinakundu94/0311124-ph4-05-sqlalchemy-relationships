from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class VideoGame(db.Model):
    __tablename__ = 'video_games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    genre = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    reviews = db.relationship('Review', backref='videogame')
    publications = association_proxy('reviews', 'publication')

    def __repr__(self):
        return f'<VideoGame id={self.id} title={self.title} genre={self.genre}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre
        }


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    videogame_id = db.Column(db.Integer, db.ForeignKey('video_games.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publications.id'))

    @validates('score')
    def validate_score(self, key, score):
        if score > 10 or score < 0:
             raise ValueError('Score must be between 0 and 10')
        return score

    def __repr__(self):
        return f'<Review id={self.id} score={self.score}>'

    def to_dict(self):
        return {
            'id': self.id,
            'score': self.score
        }

class Publication(db.Model):
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    reviews = db.relationship('Review', backref='publication')
    videogames = association_proxy('reviews', 'videogame')

    def __repr__(self):
        return f'<Publication id={self.id} name={self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }