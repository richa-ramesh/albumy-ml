import os
from flask import Flask

def create_app(config_name=None):
    app = Flask('albumy')
    
    # ... existing configuration ...
    
    # Ensure upload directory exists
    upload_path = os.path.join(app.instance_path, 'uploads')
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    app.config['ALBUMY_UPLOAD_PATH'] = upload_path
    
    return app