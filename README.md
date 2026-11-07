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
|   Gemma4:e2b  |       Gemma        |      2.3B        |    Text, image, audio        |


<br>
The models were selected to provide a comparison between different model families, sizes and capabilities to explore how these differences affect their responces to an identical prompt.<br><br>

Each model was given the same intentionally invalid syllogism using and tested using temperatures **0.0** (which favors tokens with the highest probability) and **1.0** (which introduces more variability by allowing less probable tokens to be selected). A fixed seed (4242) was also used across all models and temperature settings. <br>

The purpose of this experiment was to compare the local models' ability to identify invalid logical reasoning and to explore, to some extent, how temperature and seed parameters influence their outputs, as well as the extent to which models' responses are deterministic and reproducible under the same settings.

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
ollama pull gemma4:e2b
````

## How to Run 

Run the Python script: 

````
python ollama_test.py
````




## Results 

### 1. Response Correctness

All models provided the correct answer to the prompt: *"All men are mortal, Socrates is mortal, therefore Socrates is a man?"*, although their explanations and wording varied. Since the given prompt is a classical example of syllogism, this demonstrates that all tested local models are able to perform basic logical reasoning.


### 2. Performance 

To put the **token per second** (eval_rate), which measures the speed at which LLM generates the output text, into perspective, the [mikeveerman.github.io/tokenspeed](https://mikeveerman.github.io/tokenspeed/?rate=3.36&mode=code) can be used. It provides a visual demonstration of how different rates feel in practice.<br><br>

For comparison, Anthropic's Claude Sonnet 5.5, as reported, achieved an ouput speed of 107.1 tokens/s compared with 58.4 tokens/s for Claude Fable 5.1. [emergent.sh/learn](https://emergent.sh/learn/claude-fable-5-1-high-vs-claude-sonnet-5-5-high)

**Run 1**<br>



|     Model     |   eval_duration    |   total_duration    |   eval_rate  |  temperature     |
| ------------- | ------------------ | ------------------- | ------------ | ---------------- |
|     LFM3      |        11.831      |       13.123        | 5.510        | 0.0              |
|     LFM3      |        13.024      |       13.067        | 5.497        | 1.0              |
|   LFM3-Omni   |        2.280       |       4.474         | 6.796        | 0.0              |
|   LFM3-Omni   |        1.564       |       1.603         | 6.712        | 1.0              |
|   Qwen3.5:4B  |       27.012       |       29.865        | 2.787        | 0.0              |
|   Qwen3.5:4B  |       37.055       |       37.147        | 2.809        | 1.0              |
|   Gemma4:e2b  |       3.974        |       9.328         | 9.484        | 0.0              |
|   Gemma4:e2b  |       4.731        |       4.732         | 8.729        | 1.0              |          



<br>**Run 2**<br>



|     Model     |   eval_duration    |   total_duration    |   eval_rate  |  temperature     |
| ------------- | ------------------ | ------------------- | ------------ | ---------------- |
|     LFM3      |        12.049      |       13.996        |     5.411    | 0.0              |
|     LFM3      |        13.299      |       13.352        |     5.383    | 1.0              |
|   LFM3-Omni   |        2.261       |       4.094         |     6.854    | 0.0              |
|   LFM3-Omni   |        1.610       |       1.648         |     6.519    | 1.0              |
|   Qwen3.5:4B  |       26.756       |       29.515        |     2.814    | 0.0              |
|   Qwen3.5:4B  |       37.534       |       37.614        |     2.77     | 1.0              |
|   Gemma4:e2b  |       3.933        |       9.281         |     9.584    | 0.0              |
|   Gemma4:e2b  |       3.669        |       3.671         |     8.992    | 1.0              |  


### 3. Reproducibility and determinism

As mentioned above, a fixed seed was used across all runs. Some models produced identical responses across repeated runs, even at a temperature 1.0. However, this observation does not necessarily mean that reproducibility and determinsim can be achieved simply by using a fixed seed, as both are influenced by multiple factors. More repeated runs would be needed to draw stronger conclusuons. 

