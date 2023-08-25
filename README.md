
# Interior Design Image Generation API

This application generates interior design images based on user input using the DiffusionPipeline model. It takes in parameters such as place, dimensions, color, view, and the number of images to generate.

## Prerequisites

- Python 3.7+
- [FastAPI]
- [PyTorch]
- [diffusers]

## Installation

1. Clone this repository:
 git clone https://github.com/your-username/interior-design-api.git
 cd interior-design-api

Install the required dependencies:
pip install -r requirements.txt


## Usage

1.Run the FastAPI server:
uvicorn main:app --host 0.0.0.0 --port 8000

2.Access the API documentation: Open your web browser and go to http://localhost:8000/docs. You'll see the interactive Swagger documentation for the API.

3.Generate Interior Images: You can use the /generate_interior/ endpoint to generate interior design images. Send a POST request with the following JSON payload:

{
    "place": "Living Room",
    "dimensions": "5x4",
    "color": "Blue",
    "view": "Panoramic",
    "num_images": 3
}
4.The API will respond with a list of generated image filenames.

