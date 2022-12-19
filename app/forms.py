from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField, TextAreaField

class PostForm(FlaskForm):
    title = StringField('Title')
    text = TextAreaField('Text')
    published = BooleanField('Publish')
    submit = SubmitField('Save')

class CategoryForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Save')