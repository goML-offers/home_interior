from fastapi import FastAPI
from diffusers import DiffusionPipeline
import torch
import time
import json

app = FastAPI()

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to('cuda')

def ref(txt):
    result = ""
    for i in txt:
        result += i
        time.sleep(0.2)
    return result

def json_file(jsonfi):
    with open(jsonfi, 'r') as json_file:
        data = json.load(json_file)
    return data

def img_gen(prompt, img):
    generated_images = []
    for i in range(img):
        generated_images.append(pipe(prompt).images[0])
    return generated_images

@app.post('/generate_interior/')
async def generate_interior():
    file_path = 'home.json'  # Update with your JSON file path
    data = json_file(file_path)
    place = data['room']
    ref("hmmmm.......")
    dim = data['dim']
    ref("I think that is a fit!")
    col = data['col']
    ref("Great choice bruh ^-^")
    img = int(data['number'])
    ref('Cooking the interior . . . .')
    
    prompt = f"Home interior design top view for {place} with {col} color of dimension {dim} metre"
    images = img_gen(prompt)

    for i in range(img):
        ref(f"Generating image {i+1}...")
        image = pipe(prompt).images[0]
        image.save(f'result_{i+1}.jpg')
        images.append(image)
    
    return {
        "Message": "Successfully Generated! Check the directory to find the images",
        "images": images
    }
