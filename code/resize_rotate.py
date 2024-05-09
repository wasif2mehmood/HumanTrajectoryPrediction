# coding=utf-8
# for SDD dataset, resize and rotate to get 1920x1080 videos

import argparse
import sys
import subprocess
import os
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("videolst")
parser.add_argument("outpath")
parser.add_argument("changelst", help="save whether it is rotated")

def get_video_id(videopath):
  print(videopath)
  print('sssssssssssssssssssssssss')
  videopath_parts = videopath.split("/")
  if len(videopath_parts) < 3:
    raise ValueError("videopath must contain at least two slashes")
  return "%s_%s" % tuple(videopath_parts[-3:-1])

if __name__ == "__main__":
  args = parser.parse_args()

  target_resolution = (1920, 1080)
  if not os.path.exists(args.outpath):
    os.makedirs(args.outpath)

  changelst = []  # video_id -> original resolution, new, rotated or not
  for line in tqdm(open(args.videolst).readlines()):
    videofile = line.strip()

    video_id = get_video_id(videofile)

    # get video original resolution first to decide rotation
    size_this = '1968x1080'
    w, h = size_this.split("x")
    w, h = int(w), int(h)
    rotate_90_clockwise = False
    if h > w:
      rotate_90_clockwise = True

    vf_cmd = ""
    if rotate_90_clockwise:
      vf_cmd = "transpose=1,"
    vf_cmd += "scale=%s:%s" % target_resolution

    target_videofile = os.path.join(args.outpath, "%s.mp4" % video_id)
    print(target_videofile)
    assert not os.path.exists(target_videofile)
    print(vf_cmd)
    print(videofile)
    print(target_videofile)

    ffmpeg_cmd = ["ffmpeg", "-i", videofile, "-vf", vf_cmd, target_videofile]
    output = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print(output.stdout)

    # record the changes
    changelst.append([video_id, size_this, rotate_90_clockwise])

  with open(args.changelst, "w") as f:
    for o in changelst:
      f.writelines("%s,%s,%s\n" % (o[0], o[1], o[2]))