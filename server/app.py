#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db, Event, Session, Speaker, Bio

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


# GET /events
@app.route('/events')
def get_events():

    events = Event.query.all()

    events_data = []

    for event in events:
        events_data.append({
            "id": event.id,
            "name": event.name,
            "location": event.location
        })

    return jsonify(events_data), 200


# GET /events/<id>/sessions
@app.route('/events/<int:id>/sessions')
def get_event_sessions(id):

    event = Event.query.get(id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    sessions_data = []

    for session in event.sessions:
        sessions_data.append({
            "id": session.id,
            "title": session.title,
            "start_time": session.start_time.isoformat()
        })

    return jsonify(sessions_data), 200


# GET /speakers
@app.route('/speakers')
def get_speakers():

    speakers = Speaker.query.all()

    speakers_data = []

    for speaker in speakers:
        speakers_data.append({
            "id": speaker.id,
            "name": speaker.name
        })

    return jsonify(speakers_data), 200


# GET /speakers/<id>
@app.route('/speakers/<int:id>')
def get_speaker(id):

    speaker = Speaker.query.get(id)

    if not speaker:
        return jsonify({"error": "Speaker not found"}), 404

    bio_text = "No bio available"

    if speaker.bio:
        bio_text = speaker.bio.bio_text

    speaker_data = {
        "id": speaker.id,
        "name": speaker.name,
        "bio_text": bio_text
    }

    return jsonify(speaker_data), 200


# GET /sessions/<id>/speakers
@app.route('/sessions/<int:id>/speakers')
def get_session_speakers(id):

    session = Session.query.get(id)

    if not session:
        return jsonify({"error": "Session not found"}), 404

    speakers_data = []

    for speaker in session.speakers:

        bio_text = "No bio available"

        if speaker.bio:
            bio_text = speaker.bio.bio_text

        speakers_data.append({
            "id": speaker.id,
            "name": speaker.name,
            "bio_text": bio_text
        })

    return jsonify(speakers_data), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)