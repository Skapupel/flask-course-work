from flasksite import create_app
from os import makedirs, path, getcwd


makedirs(path.join(getcwd(), 'flasksite', 'static', 'uploads'), exist_ok=True)


app = create_app()


if __name__ == '__main__':
    app.run()