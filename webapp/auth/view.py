from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for, render_template_string,
                   flash, current_app, request)
from flask_login import login_user, logout_user, current_user
from .models import db, User, Role
from .forms import (LoginForm, RegisterForm,
                    ResetPasswordRequestForm,
                    ResetPasswordForm)
from .. import mail
from .import bcrypt
from werkzeug.utils import secure_filename
from flask_mailman import EmailMessage
from .reset_password_email_content import reset_password_email_html_content
import os


# check if the file uploaded is image with extension
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)
# the login endpoint
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, remember=form.remember.data)
        flash("You have been logged in.", category="success")
        return redirect(url_for('main.index'))
    else:
        if request.args.get('google'):
            return redirect(url_for('auth.google_login'))
    return render_template('login.html', form=form)

@auth_blueprint.route('/google-login')
def google_login():
    redirect_uri = url_for('auth.google_authorized', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth_blueprint.route('/google-authorized')
def google_authorized():
    token = google.authorize_access_token()  # get access token
    user_info = google.get('userinfo').json()  # fetch user info
    
    email = user_info['email']
    username = user_info['name']

    # Register or log in the user
    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()

    login_user(user)
    flash("Successfully logged in with Google.", "success")
    return redirect(url_for('main.index'))
# the logout endpoint
@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('main.index'))

# the registeration endpoint
@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    username = None
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        #selected_role = Role.query.get(form.role.data)
        #new_user.roles.append(selected_role)
        #new_user.specialty = form.specialty.data
        #new_user.bio = form.bio.data
        #file = form.image.data
        #if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            #new_user.image_filename = filename
        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login.", category="success")

        return redirect(url_for('.login'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    '''route to lead you to reset form'''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            send_reset_password_email(user)

        flash(
            "Instruction to reset your password were sent to your email address,"
            "if it exists in our system."
            )
        return redirect(url_for("auth.reset_password_request"))

    return render_template("auth/reset_password_request.html", title="Reset Password", form=form
    )


def send_reset_password_email(user):
    reset_password_url = url_for(
        "auth.reset_password",
        token=user.generate_reset_password_token(),
        user_id=user.id,
        _external=True,
    )

    email_body = render_template_string(
        reset_password_email_html_content, reset_password_url=reset_password_url)
    message = EmailMessage(
            subject="Reset your password",
            body=email_body,
            to=[user.email]
    )
    message.content_subtype = 'html'

    message.send()


@auth_blueprint.route('/reset_password/<token>/<int:user_id>', methods=['GET', 'POST'])
def reset_password(token, user_id):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.validate_reset_password_token(token, user_id)
    if not user:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('seccess')
        return redirect(url_for('.login'))
    return render_template(
            'auth/reset_password.html', title='Reset Password', form=form)
