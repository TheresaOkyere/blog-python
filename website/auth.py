from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def home():
    return "login"

@auth.route("/sign-up")
def sign_up():
    return "sign up"

@auth.route("/sign-out")
def sign_out():
    return "sign out"
