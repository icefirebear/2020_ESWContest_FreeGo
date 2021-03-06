import os
import unittest

from flask_script import Manager
from app.main import create_app
from app.main import db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)
manager.add_command('-dbinit', db.init_db())



@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)

@manager.command
def test():
	"""Runs the unit tests."""
	tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

if __name__ == '__main__':
	manager.run()
