import requests
from requests.auth import HTTPBasicAuth
import time
import os
import cv2
from utils.request_utils import process_and_prompt
from utils.prompts import BASIC_PROMPT

def get_raspberry_pi_image(url, username, password):
    """
    Sends a GET request to the specified URL with basic authentication and returns the image content.

    Args:
    url (str): The URL of the Raspberry Pi stream.
    username (str): The username for basic authentication.
    password (str): The password for basic authentication.

    Returns:
    bytes: The content of the image.
    """
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()  # Raise an error for bad status codes
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def stitch_images_to_video(image_folder, video_path, frame_rate):
    """
    Stitch images in the specified folder into a video.

    Args:
    image_folder (str): The folder containing images.
    video_path (str): The path to save the video.
    frame_rate (int): The frame rate of the output video.
    """
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()  # Sort images by name (which includes the timestamp)

    if not images:
        print("No images to stitch.")
        return

    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'XVID'), frame_rate, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        video.write(cv2.imread(img_path))

    video.release()
    print(f"Video saved successfully at {video_path}")

# Configuration
url = "http://mychateau.freeddns.org:60080/html/cam_pic.php"
username = "wei"
password = "santacruz"
images_folder = "images"
videos_folder = "videos"
output_folder = "output"
capture_interval = 0.02  # seconds
video_interval = 10  # seconds (e.g., create a video every 60 seconds)
frame_rate = 50  # frames per second

# Create the images, videos, and output folders if they don't exist
os.makedirs(images_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

start_time = time.time()

while True:
    current_time = time.time()
    
    # Capture images at the specified interval
    if (current_time - start_time) % capture_interval < 1:
        image_content = get_raspberry_pi_image(url, username, password)
        if image_content:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_path = os.path.join(images_folder, f"raspberry_pi_image_{timestamp}.jpg")
            with open(image_path, "wb") as image_file:
                image_file.write(image_content)
                print(f"Image saved successfully at {image_path}")
        else:
            print("Failed to retrieve the image.")

    # Create video at the specified interval
    if (current_time - start_time) % video_interval < 1:
        video_filename = f"raspberry_pi_video_{time.strftime('%Y%m%d_%H%M%S')}.avi"
        video_path = os.path.join(videos_folder, video_filename)
        stitch_images_to_video(images_folder, video_path, frame_rate)
        
        # Process video with GPT-4O
        response = process_and_prompt(video_path, BASIC_PROMPT, seconds_per_frame=1)
        output_filename = f"gpt4o_output_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        output_path = os.path.join(output_folder, output_filename)
        with open(output_path, "w") as output_file:
            output_file.write(response)
        print(f"GPT-4O output saved successfully at {output_path}")

        # Optionally, clear images after creating the video
        for img in os.listdir(images_folder):
            if img.endswith(".jpg"):
                os.remove(os.path.join(images_folder, img))

    time.sleep(1)  # Wait for 1 second to avoid tight loop
