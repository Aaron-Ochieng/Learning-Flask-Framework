from flask import Flask,render_template
from .models import db
from .config import Configuration
from .admin import administrator
from flask_migrate import Migrate

migrate = Migrate()

def create_app(configure=Configuration):
    app = Flask(__name__)
    app.config.from_object(configure)

    administrator.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.entries.routes import entries
    app.register_blueprint(entries, url_prefix='/entries')

    @app.route('/')
    def index():
        return render_template('homepage.html')
    return app
