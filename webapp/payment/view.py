import os
import stripe
from flask import Flask, jsonify, request, Blueprint, flash, redirect, url_for

payment_blueprint = Blueprint(
		    'pay',
		    __name__,
		    template_folder='../templates/payment',
		    url_prefix='/pay/'
		)
stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
}

"""
send published key to the client
html-js => publishable_key(Api-endpoint)=> js create instance
"""
@payment_blueprint.route("/config")
def get_publishable_key():
    strip_config = {'publicKey': stripe_keys['publishable_key']}
    return jsonify(strip_config)
"""
Create the session for the payment
html-js => get_checkout_session_id =?
"""
@payment_blueprint.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "https://www.robotic5333.tech/pay/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Subscription",
                        },
                        "unit_amount": 2000,  # Amount in cents
                    },
                    "quantity": 1,
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

""""
redirect if payment is success or cancelled
"""
@payment_blueprint.route("/success")
def success():
    flash('Your payment succeeded.', category="success")
    return redirect(url_for('main.index'))

@payment_blueprint.route("/cancelled")
def cancelled():
    flash('Your payment was cancelled.', category="success")
    return redirect(url_for('main.index'))


