# -*- coding: utf-8 -*-
from cloudapp import Application, BaseUser, render_template
from cloudapp.api import Blueprint as APIBlueprint, Envelope
from cloudapp.config import DebugConfig
from cloudapp.permissions import valid_user
from flask import Blueprint, request, redirect, g, url_for, json, flash, jsonify

# inherit cloudapp's debug config
class Config(DebugConfig):
    SERVER_NAME = 'example.dev:8888'
    SECRET_KEY  = 'example_secret_key'

# you need to create a www blueprint
www = Blueprint("www", __name__)
api = APIBlueprint("api")
settings = Blueprint("settings", __name__, url_prefix="/settings")

class User(BaseUser):
    pass

#
# views
#

@www.route('/typeahead')
def typeahead():
    print request.args
    return jsonify(dict(options=["Option 1", "Option 2"]))

@www.route('/')
def index():
    return render_template('splash.html')

@www.route('/profile')
@valid_user.require(http_exception=403)
def profile():
    return render_template('profile.html', user=g.identity.user)

@settings.route('/')
@valid_user.require(http_exception=403)
def profile():
    return render_template('settings/profile.html', user=g.identity.user)

@settings.route('/options')
def options():
    return render_template('settings/options.html', user=g.identity.user)

@settings.route('/emails')
def emails():
    return render_template('settings/emails.html', user=g.identity.user)

@settings.route('/social')
def social():
    return render_template('settings/social.html', user=g.identity.user)

@www.errorhandler(403)
@settings.errorhandler(403)
def permission_denied(err_code):
    return redirect( url_for('cloudapp.login') )

@api.route('/echo', methods=['PUT','POST'])
def echo():
    # the api blueprint preprocesses request.data looking for a json.
    # if a valid json is put or posted, the results of json.loads can
    # be found in g.json, otherwise g.json = None
    from flask import g
    env = Envelope()
    if g.json:
       env.add_data(g.json)
    else:
       env.add_meta('code',400)
       env.add_meta('error_message',u'unable to process json')
    return env.send()

#
# application
#

"""
 http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
"""
import os
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
def init_app(*args, **kwargs):
    flask_app = Application.flask("Example", Config, template_folder=template_folder)
    flask_app.debug = True
    app = Application(User, flask_app, **kwargs)
    flask_app.config['BOOTSTRAP_JQUERY_STATIC'] = True
    app.couch.setup(flask_app)
    app.couch.sync(flask_app)
    flask_app.register_blueprint(www)
    flask_app.register_blueprint(settings)
    flask_app.register_blueprint(api)
    return app


if __name__ == '__main__':
   users = [ dict(email='admin@example.com',password='admin!',
                  first_name="Johnny", last_name="Appleseed", roles=['Admin']) ]
   App = init_app(users=users)
   App.app.run(port=8888)
