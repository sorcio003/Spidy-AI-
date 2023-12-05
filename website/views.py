from flask import Blueprint, render_template, request, flash, jsonify, redirect
import json
from .spidy import Spidy

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/spidy/', methods=['POST'])
def talk():
    Spidy()
    return redirect('/')
        

