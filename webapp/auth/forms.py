from flask_wtf import FlaskForm as Form
from flask_wtf import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, URL, Email
from .models import User, Role
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

# check if the file uploaded is image with extension
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# login form and validater
class LoginForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)]
)
    email = StringField('email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")

    def validate(self, extra_validators=None):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our user exist
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        return True

# registration form and validater
class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=[('doctor', 'Doctor'), ('patient', 'Patient')], validators=[DataRequired()])
    specialty = StringField('Specialty')
    bio = StringField('Bio')
    image = FileField('Upload Image')
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Fetch roles from the database and set choices
        self.role.choices = [(role.id, role.name.capitalize()) for role in Role.query.all()]

    def validate(self, extra_validators=None):
        # Perform standard validation
        if not super(RegisterForm, self).validate():
            return False
        print("******************************")
        print("self.image.data : ", self.image.data)
        print("******************************")
        if self.role.data == '1' and (self.specialty.data == "" or self.bio.data == ""):
            self.specialty.errors.append('Specialty and Bio and image is required for doctors')
            return False

        # Validate the image file
        # if self.image.data is None:
        #     self.image.errors.append('Image is required for doctors')
        #     return False
        if self.image.data and self.image.data.filename:
            file_data = self.image.data
            filename = secure_filename(file_data.filename)
            if not allowed_file(filename):
                self.image.errors.append('Invalid image format')
                return False
        # Custom validation: Check if the username already exists
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("User with that name already exists")
            return False

        return True     

class ResetPasswordRequestForm(Form):
    '''form for request to change the password'''
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. you must register first')


class ResetPasswordForm(Form):
    '''Rest passwprd form'''
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Confirm Password Reset')
