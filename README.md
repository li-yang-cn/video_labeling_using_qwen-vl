# AI Video Labeling Tool 

## Background

As a part-time photographer, I possess several TBs of video materials. Finding the right footage from this vast video library without proper organization is a daunting task. To address this issue, I developed the AI Video Labeling Tool using LLM (ChatGPT for coding, qwen-vl from Tongyi Qianwen for image labeling).

## Project Description

The AI Video Labeling Tool is a Python-based tool that scans video files in a specified directory, automatically captures keyframes, and uses the large language model qwen-vl from Tongyi Qianwen to describe the video content, eventually organizing the results into a CSV format database. This tool is designed to help photographers and video creators quickly label their video material library, thereby improving the efficiency of finding resources.

## Features

- Scan video files in a specified directory (supports `.mov`, `.mp4` formats).
- Automatically capture key frames of the video and analyze the content using the large language model qwen-vl.
- Save the analysis results in CSV format for further organization and retrieval.
- Developed in Python, easy to customize and extend.

## Installation and Usage Instructions

### Prerequisites

1. Ensure you have Python 3 installed and possess basic knowledge of running Python scripts.
2. You need to register an Alibaba Cloud account and obtain an API-KEY from "Model Service Lingji". For specific pricing and details, please refer to [Alibaba Cloud official website](https://help.aliyun.com/zh/dashscope/developer-reference/api-key-settings).

### Installing Dependencies

The libraries required for the project are listed in `requirements.txt`. Install them using the following command:

```bash
pip install -r requirements.txt
```

### Setting API Key
Please specify your Alibaba Cloud API Key in the code to ensure the large language model qwen-vl can be called correctly.

### Running the Tool
Execute the following command in the project root directory:

```bash
python main.py
```
Follow the prompts to input the video file directory, and the tool will automatically start the scanning and analysis process.

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
 

## 背景

作为一名兼职摄影师，我拥有几个TB的视频素材。在没有进行适当整理的情况下，想要从这些庞大的视频库中找到合适的素材是一项极具挑战性的任务。为了解决这个问题，我借助LLM（ChatGPT编写代码、通义千问qwen-vl给图像打标签）开发了这个AI Video Labeling Tool。

## 项目介绍

AI Video Labeling Tool 是一个基于Python的工具，它可以扫描指定目录下的视频文件，自动截取关键帧，并利用通义千问的大语言模型qwen-vl对视频内容进行描述，最终将结果整理成CSV格式的数据库。这个工具旨在帮助摄影师和视频制作者快速为他们的视频素材库打标签，从而提高寻找素材的效率。

## 功能特点

- 扫描指定目录下的视频文件（支持`.mov`、`.mp4`格式）。
- 自动截取视频关键帧，并通过大语言模型qwen-vl对其进行内容分析。
- 将分析结果保存为CSV格式，便于进一步的整理和检索。
- 使用Python开发，易于定制和扩展。

## 安装使用说明

### 准备工作

1. 确保您已安装Python 3，并具有运行Python脚本的基本知识。
2. 需要注册阿里云账户，并在“模型服务灵积”中获取API-KEY。具体价格和详情请参考[阿里云官网](https://help.aliyun.com/zh/dashscope/developer-reference/api-key-settings)。

### 安装依赖

项目依赖的库在`requirements.txt`中有详细罗列，请使用以下命令安装：

```bash
pip install -r requirements.txt
```

3333 c 设置API Key

请在代码中指定您的阿里云API Key，确保大语言模型qwen-vl可以正常调用。

### 运行工具

在项目根目录下运行以下命令：
```bash
python main.py
```
按照提示输入视频文件目录，工具将自动开始扫描和分析过程。

## 许可证

本项目采用[知识共享 署名 4.0 国际许可协议 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)。

--- 
感谢您对AI Video Labeling Tool项目的关注，希望它能帮助您更高效地管理和利用您的视频素材库！  
注：以上说明及代码均又ChatGPT生成并经过人工校对。