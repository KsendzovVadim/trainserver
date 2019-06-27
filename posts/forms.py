from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField('Post Title')
    body = TextAreaField('Body')