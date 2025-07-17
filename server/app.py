from flask import Flask, make_response
from flask_migrate import Migrate
from server.models import db, Animal, Zookeeper, Enclosure


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def index():
        return '<h1>Zoo API</h1>'

    @app.route('/animal/<int:id>')
    def animal_by_id(id):
        animal = Animal.query.get(id)
        if not animal:
            return make_response(f'<h1>Animal with id {id} not found.</h1>', 404)

        response = f"<ul>\n<li>ID: {animal.id}</li>\n<li>Name: {animal.name}</li>\n<li>Species: {animal.species}</li>"
        response += f"\n<li>Zookeeper: {animal.zookeeper.name}</li>\n<li>Enclosure: {animal.enclosure.environment}</li>\n</ul>"
        return make_response(response, 200)

    @app.route('/zookeeper/<int:id>')
    def zookeeper_by_id(id):
        zk = Zookeeper.query.get(id)
        if not zk:
            return make_response(f'<h1>Zookeeper with id {id} not found.</h1>', 404)

        response = f"<ul>\n<li>ID: {zk.id}</li>\n<li>Name: {zk.name}</li>\n<li>Birthday: {zk.birthday}</li>\n"
        for animal in zk.animals:
            response += f"<li>Animal: {animal.name}</li>\n"
        response += "</ul>"
        return make_response(response, 200)

    @app.route('/enclosure/<int:id>')
    def enclosure_by_id(id):
        enc = Enclosure.query.get(id)
        if not enc:
            return make_response(f'<h1>Enclosure with id {id} not found.</h1>', 404)

        response = f"<ul>\n<li>ID: {enc.id}</li>\n<li>Environment: {enc.environment}</li>\n"
        response += f"<li>Open to Visitors: {enc.open_to_visitors}</li>\n"
        for animal in enc.animals:
            response += f"<li>Animal: {animal.name}</li>\n"
        response += "</ul>"
        return make_response(response, 200)

    return app

# Only used when running directly
if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)
