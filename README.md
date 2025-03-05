# Pinterest Video Downloader

A Flask-based web application that allows users to download videos from Pinterest by providing a video URL. The application is designed to be fast, stable, and efficient, running on a Linux server for improved performance.

## Features
- Download Pinterest videos by providing a valid URL.
- Fast and stable performance with Flask.
- Error handling to manage crashes and invalid inputs.
- Deployed on a Linux server for better reliability.
- Professional design with improved UI and responses.[Uploading pintrest_main.py…]()


## Requirements
Ensure you have the following installed:
- Python 3.x
- Flask
- Requests
  

Install dependencies using:
```bash
pip install flask requests 
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pinterest-downloader.git
   ```


## Usage
1. Start the Flask server:
   ```bash
   python pintrest_main.py
   ```

2. Open your browser and go to:
   ```
   http://localhost:5000
   ```
3. Enter a Pinterest video URL and click the download button.


## API Endpoints
- `GET /` - Loads the homepage.
- `POST /download` - Processes the video URL and returns the downloadable link.

## Contributing
Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the MIT License.

## Author
Developed by [benzene_artist ](https://github.com/Rishu-xd)

