# InstaCount
ML-based construction material counter for efficient resource management using YOLOv8 with Roboflow
Here's a README template for your project, which covers the essential details of your Flask web application for image and video inference using Roboflow.

### README.md

```markdown
# Image and Video Inference using Roboflow and Flask

This project demonstrates how to build a web application using Flask to perform image and video inference using the Roboflow API. The application allows users to upload images and videos, process them using a pre-trained model from Roboflow, and display the inference results.

## Features

- Upload images for inference using a Roboflow YOLOv5 model.
- Upload videos for inference using Roboflow's video inference API.
- Real-time prediction of uploaded media with results displayed on the web interface.
- Error handling and logging for debugging.

## Project Structure

```bash
my_flask_app/
├── app.py                  # Main Flask application
├── static/                 # Static files (uploads, images, etc.)
│   └── uploads/            # Folder where uploaded files are saved
├── templates/              # HTML templates for the web interface
│   └── index.html          # Main page template for uploading files
│   └── result.html         # Template for displaying inference results
├── README.md               # Project documentation
├── requirements.txt        # List of required dependencies
└── .gitignore              # Git ignore file for excluding certain files from version control
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Set Up Virtual Environment

Create and activate a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Roboflow API

- Create an account on [Roboflow](https://roboflow.com/) and obtain an API key.
- Set the API key in the `app.py`

### 5. Run the Application

Start the Flask server:

```bash
python app.py
```

Open a web browser and go to:

```
http://127.0.0.1:5000/
```

## Usage

1. **Image Upload**: 
   - Go to the homepage.
   - Upload an image file (allowed formats: png, jpg, jpeg, gif).
   - View the inference result on the same page.

2. **Video Upload**:
   - Upload a video file (allowed formats: mp4, mov, avi).
   - The application will process the video and display the inference results.

## Folder Structure

- `app.py`: Main backend file where Flask serves the application and handles the API calls to Roboflow.
- `templates/`: HTML templates for the web interface.
- `static/uploads/`: Folder where uploaded images and videos are saved.
- `requirements.txt`: List of Python dependencies for the project.

## Dependencies

The following dependencies are required to run the project:

- Flask
- Roboflow SDK
- Inference SDK
- OpenCV (for image and video processing)
- Werkzeug (for handling file uploads)

Install them with:

```bash
pip install -r requirements.txt
```

## API and Inference

This project uses the Roboflow API for inference. Ensure you have the correct workspace, project, and version information in your `app.py`:

```python
project = rf.workspace("YOUR_WORKSPACE").project("YOUR_PROJECT")
image_model_version = project.version(17)
video_model_version = project.version(15)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

---

### Files to Include

- **app.py**: The main Flask application.
- **templates** folder: Contains `index.html` and `result.html`.
- **static/uploads**: Directory to store uploaded files.
- **requirements.txt**: List of dependencies (you can generate this using `pip freeze > requirements.txt`).
- **README.md**: The documentation (as shown above).
- **.gitignore**: To exclude unnecessary files (such as `venv`, `__pycache__`, etc.).

### .gitignore Example

```gitignore
venv/
__pycache__/
*.pyc
static/uploads/*
.env
```

This `.gitignore` will ensure that your virtual environment and uploaded files are not included in version control.

Now you can push the project to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
``` 
