from config import create_app, db
from models import Episode, Guest, Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    e1 = Episode(date="1/11/99", number=1)
    e2 = Episode(date="1/12/99", number=2)

    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="comedian")
    g3 = Guest(name="Tracey Ullman", occupation="television actress")

    db.session.add_all([e1, e2, g1, g2, g3])
    db.session.commit()

    a1 = Appearance(rating=4, episode_id=1, guest_id=1)
    a2 = Appearance(rating=5, episode_id=2, guest_id=3)

    db.session.add_all([a1, a2])
    db.session.commit()
