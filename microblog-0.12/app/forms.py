from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    
class EditForm(Form):
    fullname = TextField('Fullname', validators = [Required()])
    email = TextAreaField('Email', validators = [Length(min = 0, max = 140)])
    android_phone = BooleanField('Do you have an android phone: (check)')
    twitter_account = BooleanField('Do you have a twitter account: (check)')
    twitter_freq = TextField("If yes, how often do you tweet? (Once a day/Several times a day/Several times per week/Fortnightly/Less frequently")
    facebook_account = BooleanField('Do you have a facebook account: (check)')
    facebook_freq = TextField("If yes, how often do you post content on Facebook?(Once per day/Weekly/Fortnightly/Less frequently")
    whatsapp_account = BooleanField('Do you have a whatsapp account: (check)')
    whatsapp_freq = TextField("If yes, how often do you use whatsapp?")
    google_plus_account = BooleanField("Do you have a google+ account?")
    google_plus_freq = TextField("If yes, how often do you post content to google+?")
    foursquare_account = BooleanField("Do you have a foursquare account?")
    foursquare_freq = TextField("If yes, how often do you check in with foursquare?")
    instagram_account = BooleanField("Do you have an instagram account?")
    instagram_freq = TextField("If yes, how often do you post content to instagram?")
    other_social_media_account = TextField("Do you have any other social media accounts?")
    other_social_media_freq = TextField("How often do you use these other accounts?")
    device_analyzer = TextField("Would you be comfortable with installing DeviceAnalyzer on your phone? (check)")
    sms_collection = TextField("Would you be comfortable with installing the Android SMS collection application on your phone? (check)")
    gmail_account = BooleanField("Do you have a gmail account?(check)")
    sharing_facebook = BooleanField("Would you be comfortable sharing your Facebook account details with us as specified in the PIL? (check)")
    sharing_whatsapp = BooleanField("Would you be comfortable sharing your Whatsapp account details with us as specified in the PIL? (check)")
    sharing_other_social_media = BooleanField("Would you be comfortable sharing your other social media details with us as specified in the PIL? (check) ")
    sharing_sms = BooleanField("Would you be comfortable sharing some or all of your SMS messages as specified in the PIL? (check)")


    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname
        
    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
        
class PostForm(Form):
    post = TextField('post', validators = [Required()])
    
class SearchForm(Form):
    search = TextField('search', validators = [Required()])

