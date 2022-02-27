from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired,FileAllowed
class UploadForm(FlaskForm):
     pic = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])