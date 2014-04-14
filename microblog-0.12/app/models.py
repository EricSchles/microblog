from app import db
from app import app
import flask.ext.whooshalchemy as whooshalchemy

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(400), unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    android_phone = db.Column(db.Boolean)
    twitter_account = db.Column(db.Boolean)
    twitter_freq = db.Column(db.SmallInteger)
    facebook_account = db.Column(db.Boolean)
    facebook_freq = db.Column(db.SmallInteger)
    whatsapp_account = db.Column(db.Boolean)
    whatsapp_freq = db.Column(db.SmallInteger)
    google_plus_account = db.Column(db.Boolean)
    google_plus_freq = db.Column(db.SmallInteger)
    foursquare_account = db.Column(db.Boolean)
    foursquare_freq = db.Column(db.SmallInteger)
    instagram_account = db.Column(db.Boolean)
    instagram_freq = db.Column(db.SmallInteger)
    other_social_media_account = db.Column(db.String(140))
    other_social_media_freq = db.Column(db.SmallInteger)
    device_analyzer = db.Column(db.Boolean)
    sms_collection = db.Column(db.Boolean)
    gmail_account = db.Column(db.Boolean)
    sharing_facebook = db.Column(db.Boolean)
    sharing_whatsapp = db.Column(db.Boolean)
    sharing_other_social_media = db.Column(db.Boolean)
    sharing_sms = db.Column(db.Boolean)

    last_seen = db.Column(db.DateTime)
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
        
    def __repr__(self):
        return '<User %r>' % (self.fullname)    
        

