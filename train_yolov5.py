
import os

os.system(
    "python train.py "
    "--img 640 "
    "--batch 10 "
    "--epochs 100 "
    "--data electric-kick-board-1/data.yaml "
    "--cfg models/yolov5s.yaml "
    "--weights yolov5s.pt "
    "--name Kickboard_yolov5s "
    "--exist-ok"
)