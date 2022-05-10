from app import create_app,db
from flask_script import Manager,Server #Shell
from app.models import * #User
# from flask_migrate import Migrate #MigrateCommand

from flask.cli import FlaskGroup


# Creating app instance
# FLASK_APP =app:create_app('development')
app = create_app('development')
cli = FlaskGroup(app)

@cli.command('test')
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@cli.command('shell')
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch=Pitch,Comment=Comment )

if __name__ == '_main_':
    cli()




# # Creating app instance
# app = create_app('development')

# manager = Manager(app)
# migrate = Migrate(app,db)

# manager.add_command('db', MigrateCommand)
# manager.add_command('server',Server)

# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User, Pitch=Pitch,Comment=Comment )

# if __name__ == '__main__':
#     manager.run()