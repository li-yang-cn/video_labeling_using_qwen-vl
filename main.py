import os
from datetime import datetime
from qwen_vl import qwen_vl
import csv
import cv2
import numpy as np

def scan_video_files(directory, extensions=['.mov', '.mp4']):
    """
    Scan the video files from specific directory
    """
    video_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                video_files.append(os.path.join(root, file))
    return video_files



def capture_frames(video_file, frame_count=5, temp_dir='frames'):
    """
    Capture `frame_count` equally spaced frames from `video_file` and save them in `temp_dir`.
    """
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 使用 OpenCV 读取视频
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise Exception("Could not open video file")

    # 获取总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算间隔
    interval = max(1, total_frames // frame_count)

    frames = []
    for i in range(frame_count):
        # 计算帧号
        frame_num = interval * i
        # 设置视频位置
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

        # 读取帧
        ret, frame = cap.read()
        if not ret:
            break

        # 保存帧
        output_path = os.path.join(temp_dir, f'{os.path.basename(video_file)}_frame_{i}.png')
        cv2.imwrite(output_path, frame)
        frames.append(output_path)

    # 释放视频
    cap.release()

    return frames



def analyze_video(video_file):
    """
    Analyze the video and output as json
    """
    frames = capture_frames(video_file)
    results_json = {}
    for i, frame in enumerate(frames):
        result = qwen_vl(frame)
        results_json[f'result{i+1}'] = result
    return results_json

def main(directory):
    video_files = scan_video_files(directory)
    with open('video_lib.csv', 'w', newline='') as csvfile:
        fieldnames = ['filename', 'directory', 'creation_time', 'result1', 'result2', 'result3', 'result4', 'result5']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for video_file in video_files:
            results_json = analyze_video(video_file)  
            record = {
                'filename': os.path.basename(video_file),
                'directory': os.path.dirname(video_file),
                'creation_time': datetime.fromtimestamp(os.path.getctime(video_file)).strftime('%Y-%m-%d %H:%M:%S'),
            }
            record.update(results_json)
            writer.writerow(record)

if __name__ == '__main__':
    #dir = input('Please input your video directory: ')
    main(directory="video")