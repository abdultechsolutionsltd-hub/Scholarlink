from database.db import db

class SavedOpportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    opportunity_id = db.Column(db.Integer, db.ForeignKey('opportunity.id'))
