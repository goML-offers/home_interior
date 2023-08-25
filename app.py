from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import DiffusionPipeline
import torch
import time

app = FastAPI()

class InteriorRequest(BaseModel):
    place: str
    dimensions: str
    color: str
    view: str
    num_images: int

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float32, use_safetensors=True, variant="fp16")
commandline_args = os.environ.get('COMMANDLINE_ARGS', "--skip-torch-cuda-test --no-half")

def generate_interior_images(prompt, num_images):
    generated_images = []
    for _ in range(num_images):
        generated_images.append(pipe(prompt).images[0])
    return generated_images

@app.post("/generate_interior/")
async def generate_interior_images_api(request: InteriorRequest):
    prompt = f"Home interior design {request.view} for {request.place} with {request.color} color of dimension {request.dimensions} metre"
    images = generate_interior_images(prompt, request.num_images)

    result_filenames = []
    for idx, image in enumerate(images, start=1):
        filename = f'result_{idx}.jpg'
        image.save(filename)
        result_filenames.append(filename)

    return {"message": "Images generated successfully", "image_filenames": result_filenames}
