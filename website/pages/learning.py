from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
import os
import concurrent.futures
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video


print("Hello")

learning_page = Blueprint ('learning_page', __name__, template_folder='/templates')

print("Hello2")

import concurrent.futures

def generate_video_async(prompt, video_path):
    """Run the generate_video function asynchronously"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(generate_video, prompt, video_path)
        return future
    

def generate_video(prompt: str, output_path: str):
    """
    Generates a video based on a given text prompt using the Hugging Face diffusion model.
    """

    print(f"Started generating video for prompt: {prompt}")
    pipe = DiffusionPipeline.from_pretrained(
        "damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16"
    )
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()

    

    video_frames = pipe(prompt).frames
    export_to_video(video_frames, output_path)

    print(f"Video generation completed. File saved at: {output_path}")

    return output_path


@learning_page.route('/learning', methods=['GET'])
@login_required
def learning():
    # Define the video path
    video_path = os.path.join('website', 'static', 'learning_videos', 'learning_video.mp4')

    # Check if the video file exists
    if not os.path.exists(video_path):
        # Trigger the video generation asynchronously
        future = generate_video_async("A beautiful landscape with mountains", video_path)
        print("Video generation has started asynchronously.")
        # Return a loading message or a different page while the video is being generated
        return render_template("learning.html", user=current_user, video_url=None)
    
    # If the video exists, render it
    return render_template("learning.html", user=current_user, video_url='/static/learning_videos/learning_video.mp4')


# # Necessary imports for video generation
# import torch
# from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
# from diffusers.utils import export_to_video

# # Define the function directly in the same file
# def generate_video(prompt: str, output_path: str):
#     """
#     Generates a video based on a given text prompt using the Hugging Face diffusion model.
#     """
#     pipe = DiffusionPipeline.from_pretrained(
#         "damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16"
#     )
#     pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
#     pipe.enable_model_cpu_offload()
#     pipe.enable_vae_slicing()

#     video_frames = pipe(prompt).frames
#     export_to_video(video_frames, output_path)

#     return output_path

# # Define your blueprint and routes
# learning_page = Blueprint('learning_page', __name__, template_folder='/templates')

# @learning_page.route('/learning', methods=['GET'])
# @login_required
# def learning():
#     # Define the video path
#     video_path = os.path.join('website', 'static', 'learning_videos', 'learning_video.mp4')
    
#     # Generate the video using a prompt
#     generate_video("A beautiful landscape with mountains", video_path)
#     print("Video is being generated")

#     # Render the learning page and pass the video URL to the template
#     return render_template("learning.html", user=current_user, video_url='/static/videos/learning_video.mp4')

# @learning_page.route('/download_video', methods=['GET'])
# @login_required
# def download_video():
#     video_path = os.path.join('website', 'static', 'learning_videos', 'learning_video.mp4')
#     return send_file(video_path, as_attachment=True)


# @learning_page.route ('/learning', methods = ['GET'])
# @login_required
# def learning ():
#     return render_template ("learning.html", user=current_user)