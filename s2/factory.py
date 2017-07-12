import pymongo
from flask import Flask

from s2.blueprints.properties import views as prop_views
from s2.blueprints.frontend import views as frontend_views


def create_app(config=None):
    app = Flask('s2', static_folder='blueprints/frontend/static')
    app.config.from_object('s2.conf.ProductionConfig')
    app.config.update(config or {})
    app.db = pymongo.MongoClient(
        app.config['MONGO_HOST'])[app.config['MONGO_DBNAME']]
    app.register_blueprint(prop_views.bp, url_prefix='/api')
    app.register_blueprint(frontend_views.bp)

    return app
