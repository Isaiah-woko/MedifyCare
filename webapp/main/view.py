from flask import Blueprint, redirect, url_for, render_template, make_response

main_blueprint = Blueprint(
		    'main',
		    __name__,
		    template_folder='../templates',
		    url_prefix='/'
		)


@main_blueprint.route('/')
def index():
    # Create a response object
	response = make_response(render_template('main.html'))

    # Set a cookie with 'SameSite=None' and 'Secure=True'
	response.set_cookie('my_cookie', 'cookie_value', samesite='None', secure=True)

    # Return the response object
	return response
		
