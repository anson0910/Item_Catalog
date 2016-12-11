from flask import render_template, Blueprint, flash, redirect, url_for, request
# from sqlalchemy import create_engine, asc
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, User, Category, Item
from flask import session as login_session
import random
import string
# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import FlowExchangeError
import httplib2
import json
# from flask import make_response
# import requests


# CLIENT_ID = json.loads(
#     open('client_secrets.json', 'r').read())['web']['client_id']
user_api = Blueprint('user_api', __name__)
#
# # Connect to Database and create database session
# engine = create_engine('sqlite:///catalogwithusers.db')
# Base.metadata.bind = engine
#
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


