from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
import os

print("Hello")

learning_page = Blueprint ('learning_page', __name__, template_folder='/templates')

print("Hello2")

import concurrent.futures

def generate_video_async(prompt, video_path):
    """Run the generate_video function asynchronously"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(generate_video, prompt, video_path)
        return future

@learning_page.route('/learning', methods=['GET'])
@login_required
def learning():
    # Define the video path
    video_path = os.path.join('website', 'static', 'learning_videos', 'learning_video.mp4')

    # Trigger the video generation asynchronously
    future = generate_video_async("A beautiful landscape with mountains", video_path)

    # Optionally, you can monitor the `future` to check its status if needed
    print("Video generation has started asynchronously.")

    # Render the learning page and pass the video URL to the template
    return render_template("learning.html", user=current_user, video_url='/static/videos/learning_video.mp4')
