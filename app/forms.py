from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    subject = StringField('subject',validators=[DataRequired()])
    body = StringField('Message',validators=[DataRequired()])
    # submit = SubmitField(label=('Submit'))    


