from flask import request, jsonify
from flask_cors import CORS
from config import create_app, db
from models import Episode, Guest, Appearance

app = create_app()
CORS(app)

@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        e.to_dict(only=('id', 'date', 'number'))
        for e in episodes
    ]), 200

@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(
        episode.to_dict(
            include={
                'appearances': {
                    'only': ('id', 'rating', 'guest_id', 'episode_id'),
                    'include': {
                        'guest': {
                            'only': ('id', 'name', 'occupation')
                        }
                    }
                }
            }
        )
    ), 200

@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    db.session.delete(episode)
    db.session.commit()
    return '', 204

@app.route('/guests')
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        g.to_dict(only=('id', 'name', 'occupation'))
        for g in guests
    ]), 200

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(
            appearance.to_dict(
                include={
                    'episode': {'only': ('id', 'date', 'number')},
                    'guest': {'only': ('id', 'name', 'occupation')}
                }
            )
        ), 201
    except Exception:
        return jsonify({"errors": ["validation errors"]}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
