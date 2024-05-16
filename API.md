# Adding a New API

To add a new API endpoint to the Flask application, follow these steps:

1. Open `app.py` in your preferred text editor.

2. Define a new route function. For example:
    ```python
    @app.route('/new-api', methods=['GET', 'POST'])
    def new_api():
        if request.method == 'POST':
            data = request.json
            # Process the data
            return jsonify({'status': 'success', 'message': 'Data received'}), 201
        else:
            return jsonify({'status': 'success', 'message': 'GET request successful'}), 200
    ```

3. If the new API requires database interactions, make sure to import the necessary models and handle the database session appropriately.

4. Test your new API using tools like Postman or curl to ensure it behaves as expected.

5. Commit your changes and push to your repository.

Example of a complete new API route:

```python
from flask import Flask, request, jsonify
from db import app, db, NewModel

@app.route('/new-api', methods=['GET', 'POST'])
def new_api():
    if request.method == 'POST':
        data = request.json
        new_entry = NewModel(field1=data['field1'], field2=data['field2'])
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Data received'}), 201
    else:
        return jsonify({'status': 'success', 'message': 'GET request successful'}), 200

