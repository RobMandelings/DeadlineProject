import uuid

import sys

import click
import flask
import flask_cors
import database.database as database
import config

# TODO import server.src.config as config
import flask.cli as cli


def init_cli_commands(app):
    """
    Initializes commands which can be used by the flask commandline
    :param app: instance of the flask application
    :return: void
    """
    app.cli.add_command(init_db_command)


@click.command('init-db')
@cli.with_appcontext
def init_db_command():
    # TODO niet hier importeren?
    database.init_db()
    click.echo('Initialized the database')


def init_app(config_type='development'):
    """
    Initializes the flask server application, creating an 'app' instance, loading in configurations and setting up the
    database system.
    :param config_type: development, production
    :return: the instanced flask app
    """
    # instantiate the app
    app = flask.Flask(__name__)
    app.config.from_object(config.config[config_type])
    init_cli_commands(app)
    database.db.init_app(app)

    # enable CORS
    # It's worth noting that the above setup allows cross-origin requests on all routes, from any domain, protocol, or port.
    # In a production environment, you should only allow cross-origin requests from the domain where the front-end application is hosted.
    # Refer to the Flask-CORS documentation for more info on this.
    flask_cors.CORS(app, resources={r'/*': {'origins': '*'}})

    return app


if len(sys.argv) > 2:
    app = init_app(sys.argv[2])
else:
    app = init_app()

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


# @app.route('/books', methods=['GET', 'POST'])
# def all_books():
#     response_object = {'status': 'success'}
#     if request.method == 'POST':
#         post_data = request.get_json()
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book added!'
#     else:
#         response_object['books'] = BOOKS
#     return jsonify(response_object)
#
#
# @app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
# def single_book(book_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book updated!'
#     if request.method == 'DELETE':
#         remove_book(book_id)
#         response_object['message'] = 'Book removed!'
#     return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')


if __name__ == '__main__':
    app.run()
