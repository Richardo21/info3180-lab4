from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed



class UploadForm(FlaskForm):
    photo = FileField('Select a photo', validators = [FileRequired(), FileAllowed(['jpg', 'png'],'Images Only!')])