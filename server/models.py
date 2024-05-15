from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
# wait what the heck is an association proxy?

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# BUILD OUT THE FOLLOWING MODELS

# YOU WILL NEED ADDITIONAL COLUMNS FOR THE FOREIGN KEYS


# VideoGame #########
# id        integer #
# name     string  #
#####################

class VideoGame(db.Model):
    pass

    __tablename__ = 'video_games_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


    reviews = db.relationship("Reviews", back_populates='videogame')

    publications = association_proxy('reviews', 'publication')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "publications": [pub.to_dict() for pub in self.publication]
        }
    
   

# Publication #######
# id        integer #
# name      string  #
#####################




# Rating ############
# id        integer #
# rating    integer  #
#####################

class Publication(db.Model):

    __tablename__ = 'publications_table'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='publication')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name 
        }

class Review(db.Model):
    __tablename__ = 'reviews_table'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default=0)

    videogame_id = db.Column(db.Integer, db.ForeignKey('video_games_table.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publications_table.id'))

    publication = db.relationship('Publication', back_populates='reviews')
    videogames = db.relationship('Videogame', back_populates='reviews')

    def to_dict(self):
        return{
            "id": self.id,
            "rating": self.rating,
            "videogame_id": self.videogame_id,
            "publication_id": self.publication_id
        }
    
    def __repr__(self):
        return f"Review(id{self.id}, rating={self.rating}, publication={self.publication.name})"