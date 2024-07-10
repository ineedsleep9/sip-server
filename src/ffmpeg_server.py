import subprocess
import os
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor or ProcessPoolExecutor
from utils.request_utils import process_and_prompt  # Import your processing function
from utils.prompts import BASIC_PROMPT
from agents.fall_detection_agent import test_for_fall
from agents.action_planning_agent import plan_actions

# RTSP stream URL
RTSP_URL = "rtsp://169.233.151.219:8554/cam_with_audio"

# Directory to save clips
SAVE_DIR = "saved_clips"
os.makedirs(SAVE_DIR, exist_ok=True)
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

future = None

def pipeline(filename):
    # Test for a fall
    fall_detected = test_for_fall(filename)

    if fall_detected:
        # Plan actions
        response = plan_actions(filename)
    else:
        response = "No fall detected. No action needed."

    return response

# Function to capture and process video
def capture_and_process():
    while True:
        # Generate a unique filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(SAVE_DIR, f"clip_{timestamp}.mp4")

        # FFmpeg command to capture a 10-second chunk from the RTSP stream
        ffmpeg_command = [
            "ffmpeg",
            "-i", RTSP_URL,
            "-t", "10",
            "-c", "copy",
            filename
        ]

        # Execute FFmpeg command
        subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(f"Saved 10-second clip to {filename}")
        global future
        if future is not None:
            # Wait for the previous processing task to complete
            response = future.result()
            output_path = os.path.join(OUTPUT_DIR, f"gpt4o_output_{timestamp}.txt")
            with open(output_path, "w") as output_file:
                output_file.write(response)


        # Process the video asynchronously
        future = executor.submit(pipeline, filename)  # Adjust parameters as needed

        # Sleep for a short time to avoid overlapping chunks (optional)
        time.sleep(1)

# Prompt for ChatGPT processing (example)
prompt = "Describe the scene in the video."

# Set up ThreadPoolExecutor with desired number of threads
executor = ThreadPoolExecutor(max_workers=2)  # Adjust max_workers as needed

# Start capturing and processing videos
capture_and_process()
