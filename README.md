# Local LLM comparison 

## Introduction

This project explores and compares the performance of the different Large Language Models (LLMs) running locally using Ollama.

The following models were selected for this experiment:<br><br>


|     Model     |    Model Family    |    Parameters    |           Input              |
| ------------- | ------------------ | ---------------- | ---------------------------- |
|     LFM3      |        LFM         |       1.7B       |            Text              |
|               |                    |                  |                              |
|   LFM3-Omni   |        LFM         |       2.17B      | Text, images, video, audio   |
|               |                    |                  |                              |
|   Qwen3.5:4B  |       Qwen         |        4B        |         Text, image          |
|               |                    |                  |                              |


<br>
The models were selected to provide a comparison between different model families, sizes and capabilities to explore how these differences affect their responces to identical prompts. 

## Setup and Requirements 

### Requirements

* Python 3.12 or later 
* Ollama 
* Ollama Python library

### 1. Install Ollama 

#### **macOS**

Download and install Ollama via [ollama.com/download](https://ollama.com/download).<br>
Alternatively, install it using the terminal:<br>

````
curl -fsSL https://ollama.com/install.sh | sh
````
#### **Windows**

Download and install Ollama via [ollama.com/download/windows](https://ollama.com/download/windows).<br>
Alternatively, install it using the terminal:<br>

````
irm https://ollama.com/install.ps1 | iex
````

### 2. Clone the repository

````
git clone https://github.com/HejKatja/DV066G-AI-Engineering.git
````

### 3. Install Python package

````
pip install ollama
````

### 4. Download the models

````
ollama pull lfm3:latest 
ollama pull lfm3-omni:latest 
ollama pull qwen3.5:4b
````

## How to Run 

Run the Python script: 

````
python ollama_test.py
````




## Results 


## Conclusion 