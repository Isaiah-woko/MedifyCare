from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for,
                   flash, current_app, request)
from flask_login import login_user, logout_user
from .models import db, User, Role
from .forms import LoginForm, RegisterForm
from werkzeug.utils import secure_filename
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
        user = User.query.filter_by(username=form.username.data).one()
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
        user = User(username=username, email=email)
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
    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)
        selected_role = Role.query.get(form.role.data)
        new_user.roles.append(selected_role)
        new_user.specialty = form.specialty.data
        new_user.bio = form.bio.data
        file = form.image.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            new_user.image_filename = filename
        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login.", category="success")

        return redirect(url_for('.login'))

    return render_template('register.html', form=form)

