from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from .. import db
from ..auth.models import User, Role
main_blueprint = Blueprint(
		    'main',
		    __name__,
		    template_folder='../templates',
		    url_prefix='/'
		)


@main_blueprint.route('/')
def index():
	doctors = db.session.query(
        User.username).all()
        #User.specialty,
        #User.bio,
		#User.image_filename
        # User.is_available  # Assuming you have a field for availability
    #).join(User.roles).filter(Role.name == 'doctor').all()

	#specialties = list(set(doctor.specialty for doctor in doctors))
	return render_template('home.html',doctors= doctors)	

