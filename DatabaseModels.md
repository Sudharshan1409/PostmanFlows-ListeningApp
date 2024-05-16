# Adding a New Database Model

To add a new database model to the Flask application, follow these steps:

1. Open `db.py` in your preferred text editor.

2. Define a new model class. For example:
    ```python
    class NewModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        field1 = db.Column(db.String(255), nullable=False)
        field2 = db.Column(db.Text, nullable=False)
    ```

3. Import and use the new model in `app.py` where necessary.

4. Create a new migration script:
    ```bash
    flask db migrate -m "Added NewModel"
    ```

5. Apply the migration to update the database schema:
    ```bash
    flask db upgrade
    ```

Example of adding a new model:

```python
# db.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class NewModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(255), nullable=False)
    field2 = db.Column(db.Text, nullable=False)

