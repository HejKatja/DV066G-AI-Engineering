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

Each model was given the same intentionally invalid syllogism and was tested using temperatures **0.0** (which favors tokens with the highest probability) and **1.0** (which introduces more variability by allowing less probable tokens to be selected). A fixed seed (4242) was also used across all models and temperature settings. <br>

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

#### Observations:<br>

- All models identified the argument as logically invalid when responding to the prompt: "*All men are mortal, Socrates is mortal, therefore Socrates is a man*?", although their explanations and wording varied. This was consistent across both temperature settings. However, not all models were able to provide a correct explanation, as, for example, demonstrated by **lfm3-omni:latest** at both temperature 0.0 and 1.0 run in Katja’s run.


#### Conclusions:<br>

- The results suggest that reaching the correct conclusion does not necessarily mean that a model has performed the underlying logical reasoning correctly.



### 2. Performance 

#### Observations:<br>

- Regarding the **token per second**, **Gemma4** appears to be the fastest model, followed by **LFM3** and **LFM3-Omni**. However, the same model achieved different speeds across different conputers, indicating that hardware has a significant impact on model's performance.<br><br>

    
    >Note:<br>
    >To put the **token per second**, which measures the speed at which LLM generates the output text, into perspective, the [mikeveerman.github.io/>tokenspeed](https://mikeveerman.github.io/tokenspeed/?rate=3.36&mode=code) can be used. It provides a visual demonstration of how different rates >feel in practice. For comparison, Anthropic's Claude Sonnet 5.5, as reported, achieved an ouput speed of 107.1 tokens/s compared with 58.4 tokens/s >for Claude Fable 5.1. [emergent.sh/learn](https://emergent.sh/learn/claude-fable-5-1-high-vs-claude-sonnet-5-5-high)

<br>

#### Katja. Run 1<br>



|     Model     |   eval_duration    |   total_duration    |   tokens/s   |  temperature     |
| ------------- | ------------------ | ------------------- | ------------ | ---------------- |
|     LFM3      |        21.62       |       23.02         | 52.3         | 0.0              |
|     LFM3      |        31.95       |       31.99         | 56.2         | 1.0              |
|   LFM3-Omni   |        5.05        |       7.04          | 69.0         | 0.0              |
|   LFM3-Omni   |        2.12        |       2.16          | 68.4         | 1.0              |
|   Qwen3.5:4B  |       82.56        |       85.34         | 28.5         | 0.0              |
|   Qwen3.5:4B  |       76.52        |       76.59         | 28.4         | 1.0              |
|   Gemma4:e2b  |       4.92         |       10.33         | 90.7         | 0.0              |
|   Gemma4:e2b  |       8.45         |       8.45          | 86.3         | 1.0              |        
<br>


#### Mohamed. Run 1<br>



|     Model     |   eval_duration    |   total_duration    |   eval_rate  |  temperature     |
| ------------- | ------------------ | ------------------- | ------------ | ---------------- |
|     LFM3      |        12.05       |       17.86         |     90.2     | 0.0              |
|     LFM3      |        36.77       |       36.82         |     87.1     | 1.0              |
|   LFM3-Omni   |        3.61        |       8.4           |     96.9     | 0.0              |
|   LFM3-Omni   |        3.72        |       3.77          |     94.2     | 1.0              |
|   Qwen3.5:4B  |       40.33        |       47.57         |     39.7     | 0.0              |
|   Qwen3.5:4B  |       34.64        |       34.77         |     39.6     | 1.0              |
|   Gemma4:e2b  |       9.06         |       21.28         |     85.4     | 0.0              |
|   Gemma4:e2b  |       7.57         |       7.62          |     86.1     | 1.0              |  
<br>


#### Wessam. Run 1<br>



|     Model     |   eval_duration    |   total_duration    |   eval_rate  |  temperature     |
| ------------- | ------------------ | ------------------- | ------------ | ---------------- |
|     LFM3      |        117.49      |       126.23        |     8.4      | 0.0              |
|     LFM3      |        227.14      |       228.2         |     8.5      | 1.0              |
|   LFM3-Omni   |        59.82       |       77.15         |     6.3      | 0.0              |
|   LFM3-Omni   |        49.89       |       51.28         |     7.5      | 1.0              |
|   Qwen3.5:4B  |       464.59       |       549.77        |     3.3      | 0.0              |
|   Qwen3.5:4B  |       462.7        |       464.15        |     3.5      | 1.0              |
|   Gemma4:e2b  |       103.12       |       251.88        |     8.0.     | 0.0              |
|   Gemma4:e2b  |       129.87       |       130.38        |     6.9      | 1.0              |  


#### Conclusions:<br>

- **Token per second** cannot be considered as an objective measurement of a model's capabilities, since it depends not only on the model but also on the hardware used. Differences in **token per second** may, therefore, reflect hardware differencies rather than differences in model perfomance.

- Some of the models tested reached or even exceeded the reported speed of Claude Fable 5.1. However, this does not reflect overall model capabilities, nor does it mean that the same speed would be achieved with every prompt. 


### 3. Reproducibility and determinism

#### Observations:<br>

- Repeated runs on the same computer produced identical responses in most cases. 

- Responces were not identical across different hardware. 

- **LFM3-Omni** tends to produce identical responses at temperature 0 and 1. 


#### Conclusions:<br>

- Althought, a fixed seed was used across all runs, identical responses were not guaranteed, even at a temperature of 0.0. Repeated runs on the same computer produced identical responses in the most cases, while differences were observed across computers with different hardware. This indicates that neither a fixed seed nor a temperature of 0.0 alone guarantees deterministic output, as reproducibility depends on several factors (floating-point calculations, CPU thread scheduling etc.)