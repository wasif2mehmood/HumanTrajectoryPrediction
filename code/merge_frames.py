import cv2
import os
import argparse
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def merge_frames_to_video(input_dir, output_file, fps):
    images = [img for img in os.listdir(input_dir) if img.endswith(".jpg")]
    images.sort(key=natural_keys)

    frame = cv2.imread(os.path.join(input_dir, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(input_dir, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge frames into a video.')
    parser.add_argument('dir', type=str, help='Directory containing the frames')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second')
    args = parser.parse_args()

    output_file = os.path.join(args.dir, 'output.mp4')
    merge_frames_to_video(args.dir, output_file, args.fps)