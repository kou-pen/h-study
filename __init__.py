from flask import Flask

app = Flask(__name__)
app.config.from_object('mysite.config')

#import flask_blog.views
