# End-to-end-medical-chatbot
End-to-end-medical-chatbot


## Steps to run project

#### STEP: 01 - Create a virtual environment

create a conda virtual environment

```bash
conda create -n venv python=3.10 -y
```

To activate environment, use

```bash
conda activate venv
```

#### STEP: 02 - Install the required packages

```bash
pip install -r requirements.txt
```

#### STEP: 03 - Create a .env file in your root directory and add pinecone credentials as follows

```ini
PINECONE_API_KEY = <PINECONE_API_KEY>
PINECONE_API_HOST = <PINECONE_API_HOST>
PINECONE_INDEX_NAME = <PINECONE_INDEX_NAME>
```

#### STEP: 04 - Download the quantized model from link provided in model folder and keep model in the model directory

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```