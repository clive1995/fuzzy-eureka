from app.main import create_app
from app import blueprint
from app.main import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app('LOCAL')
app.register_blueprint(blueprint)
app.app_context().push()
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    # manager.run()
    app.run(debug=True)
