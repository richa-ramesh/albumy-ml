# Albumy

*Capture and share every wonderful moment.*
# Albumy ML - AI-Enhanced Photo Sharing Application

Enhanced version of Albumy with machine learning-powered accessibility and search features.
> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Features

- **Automatic Alt Text Generation**: AI generates descriptive alternative text for uploaded images
- **Intelligent Image Search**: Search photos by AI-detected objects and content
- **Manual Alt Text Override**: Users can provide custom accessibility descriptions
- **No External APIs Required**: Works completely offline with intelligent fallback system

## Requirements

- Python 3.10.x
- Flask and associated web framework dependencies
- PIL/Pillow for image processing
- SQLAlchemy for database management

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/richa-ramesh/albumy-ml.git
cd albumy-ml
```

### 2. Create Virtual Environment
```bash
python3.10 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
export FLASK_APP=albumy.py

# Create database tables
flask shell
# In the Flask shell, run:
# from albumy import db
# from albumy.models import *
# db.create_all()
# exit()

# Generate sample data
flask forge
```

### 5. Run the Application
```bash
flask run
```

The application will be available at: http://127.0.0.1:5000

## Test Account

- **Email**: `admin@helloflask.com`
- **Password**: `helloflask`

## Usage

### Uploading Photos
1. Navigate to the upload page
2. Select an image file
3. Optionally provide description and custom alt text
4. If no alt text is provided, AI will generate it automatically
5. Upload the photo

### Searching Photos
1. Use the existing search functionality
2. Search terms will match against:
   - Photo descriptions
   - Generated alt text
   - Detected objects and keywords
3. Search works with keywords like: "photo", "picture", "image", or filename-based keywords

### Accessibility Features
- All uploaded images automatically receive alt attributes
- Screen readers can access meaningful descriptions
- Manual override available for custom accessibility text

## AI System Details

The application uses a fallback AI system that:
- Analyzes filenames for descriptive keywords
- Performs basic image property analysis
- Generates searchable object tags
- Works entirely offline without external API dependencies

**Pro Tip**: For better AI analysis, use descriptive filenames like:
- `beach_sunset.jpg` → Generates "Photo of beach, sunset"
- `family_dog_park.jpg` → Generates "Photo with family, dog, park"
- `birthday_celebration.jpg` → Generates "Photo of birthday, celebration"

## Technical Architecture

- **Backend**: Flask web framework with SQLAlchemy ORM
- **Database**: SQLite with enhanced schema for ML data
- **ML Service**: Custom fallback system using filename analysis and image properties
- **Frontend**: Bootstrap-based responsive web interface
- **Image Processing**: Pillow (PIL) for image manipulation and analysis

## File Structure

- `albumy/ml_service.py` - ML processing and analysis logic
- `albumy/models.py` - Database schema with ML-enhanced Photo model
- `albumy/blueprints/main.py` - Upload and search route handlers
- `albumy/templates/` - HTML templates with accessibility enhancements
- `requirements.txt` - Python 3.10 compatible dependencies

## Development Notes

This implementation prioritizes:
- **Accessibility**: All images have meaningful alt text
- **Privacy**: No external API calls, all processing local
- **Reliability**: Robust fallback system with error handling
- **Scalability**: Efficient database queries and indexed searches
- **Maintainability**: Clean separation of ML logic and web application

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project extends the original Albumy application and maintains its MIT license.

## Acknowledgments

- Original Albumy application by Grey Li
- Enhanced with ML capabilities for CS 516 coursework
- Developed using Python 3.10 and modern Flask ecosystem

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
