#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, VideoGame, Publication, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)



# ROUTES #


@app.get('/')
def index():
    return "Hello World"


# VideoGame ROUTES #

@app.get('/video-games')
def video_games_index():
    return [ v.to_dict() for v in VideoGame.query.all() ], 200


@app.get('/video-games/<int:id>')
def video_game_by_id(id):
    vg = VideoGame.query.where(VideoGame.id == id).first()
    if vg:
        return vg.to_dict(), 200
    else:
        return { 'error': 'Not found' }, 404


@app.post('/video-games')
def post_video_game():
    vg = VideoGame(name=request.json.get('name'))
    db.session.add(vg)
    db.session.commit()
    return vg.to_dict()


@app.delete('/video-games/<int:id>')
def delete_video_games():
    vg = VideoGame.query.where(VideoGame.id == id).first()
    if vg:
        db.session.delete(vg)
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404



# Publication ROUTES #

@app.get('/publications')
def publications_index():
    return [ p.to_dict() for p in Publication.query.all() ], 200


@app.get('/publications/<int:id>')
def publication_by_id(id):
    pub = Publication.query.where(Publication.id == id).first()
    if pub:
        return pub.to_dict(), 200
    else:
        return { 'error': 'Not found' }, 404


@app.post('/publications')
def post_publication():
    pub = Publication(name=request.json.get('name'))
    db.session.add(pub)
    db.session.commit()
    return pub.to_dict()


@app.delete('/publications/<int:id>')
def delete_publication():
    pub = Publication.query.where(Publication.id == id).first()
    if pub:
        db.session.delete(pub)
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404



# Review ROUTES #

@app.get('/reviews')
def reviews_index():
    return [ r.to_dict() for r in Review.query.all() ], 200


@app.get('/reviews/<int:id>')
def review_by_id(id):
    rev = Review.query.where(Review.id == id).first()
    if rev:
        return rev.to_dict(), 200
    else:
        return { 'error': 'Not found' }, 404


@app.post('/reviews')
def post_review():
    rev = Review(
        rating=request.json.get('rating'),
        videogame_id=request.json.get('videogame_id'),
        publication_id=request.json.get('publication_id')
    )
    db.session.add(rev)
    db.session.commit()
    return rev.to_dict()


@app.delete('/reviews/<int:id>')
def delete_review():
    rev = Review.query.where(Review.id == id).first()
    if rev:
        db.session.delete(rev)
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404



# RUN APP #

if __name__ == '__main__':
    app.run(port=5555, debug=True)
