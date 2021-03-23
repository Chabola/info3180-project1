from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField(u'Property Title', [validators.DataRequired()])

    desc = TextAreaField(u'Description', [validators.DataRequired()])

    rooms = StringField(u'No. of Rooms', [validators.DataRequired()])

    bath = StringField(u'No. of Bathrooms', [validators.DataRequired()])

    price = StringField(u'Price', [validators.DataRequired()])

    type = SelectField(u'Property Type', [validators.InputRequired()], choices=["House", "Apartment"])

    location = StringField(u'Location', [validators.DataRequired()])

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])

    submit = SubmitField('Add property')
