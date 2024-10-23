import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

def generate_video(prompt: str, output_path: str):
    """
    Generates a video based on a given text prompt using the Hugging Face diffusion model.
    """
    pipe = DiffusionPipeline.from_pretrained(
        "damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16"
    )
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()

    video_frames = pipe(prompt).frames
    export_to_video(video_frames, output_path)

    return output_path
