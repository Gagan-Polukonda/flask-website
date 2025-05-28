from flask import Flask
from routes.views import views
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Register blueprints
    app.register_blueprint(views, url_prefix='/views')
    
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(port=7000)
