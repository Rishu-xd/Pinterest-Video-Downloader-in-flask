# app.py (backend)
from flask import Flask, request, jsonify, render_template, Response
import requests
import re

app = Flask(__name__)

def get_pinterest_video_url(page_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()

        video_url_match = re.search(r'"url":"(https://v\d+\.pinimg\.com/videos/[^"]+\.mp4)"', response.text)
        if video_url_match:
            return video_url_match.group(1).replace("\\", "")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():
    page_url = request.form.get('url')
    if not page_url:
        return jsonify({"error": "Please enter a Pinterest URL"}), 400

    video_url = get_pinterest_video_url(page_url)
    if not video_url:
        return jsonify({"error": "Couldn't find a video in this Pinterest link"}), 400

    return jsonify({"video_url": video_url})

@app.route('/download-file')
def download_file():
    video_url = request.args.get('url')
    req = requests.get(video_url, stream=True)
    return Response(
        req.iter_content(chunk_size=1024),
        headers={
            "Content-Disposition": f"attachment; filename=pinterest_video.mp4",
            "Content-Type": req.headers['Content-Type']
        }
    )

if __name__ == "__main__":
    app.run(debug=True)