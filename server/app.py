#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Review, VideoGame

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Index for VideoGame/Review API"

# GAMES #

@app.get('/videogames')
def games():
    games = [game.to_dict() for game in Game.query.all()]
    return games, 201


@app.post('/videogames')
def create_game():
    # try:
    game = VideoGame(
        title=request.json.get('title'),
        genre=request.json.get('genre'),
    )
    db.session.add(game)
    db.session.commit()
    return game.to_dict(), 201
    # except:
    #     return { 'message': 'Failed to create game' }, 406

@app.get('/videogames/<int:id>')
def game_by_id(id):
    game = VideoGame.query.filter(VideoGame.id == id).first()
    try:
        return game.to_dict(), 200
    except AttributeError:
        return {'message': 'No game found'}, 404


@app.patch('/videogames/<int:id>')
def patch_game(id):
    game = VideoGame.query.filter(VideoGame.id == id).first()
    if game:
        for attr in request.json:
            setattr(game, attr, request.json.get(attr))

        db.session.add(game)
        db.session.commit()

        return game.to_dict(), 202
    else:
        return {'message': 'Game not found'}, 404


@app.delete('/videogames/<int:id>')
def delete_game(id):
    game = VideoGame.query.filter(VideoGame.id == id).first()
    if game:
        game_reviews = game.reviews
        for review in game_reviews:
            db.session.delete(review)
        db.session.delete(game)
        db.session.commit()
        return {'message': 'Game deleted'}, 202
    else:
        return {'message': 'No game found'}, 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
