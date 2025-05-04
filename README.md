# Local Reasoning Chatbot using Ollama and qwen3 Model

This project sets up a chatbot locally using [Ollama](https://ollama.com) and the qwen3 model.

![Chatbot Screenshot](1.png)

## Prerequisites

- **Operating System**: Windows, macOS, or Linux
- **Ollama**: Installed locally. [Download Ollama](https://ollama.com/download)
- **Terminal or command line access**
- **Python (Optional)**: For frontend/backend integration

## Model Used

- **Model**: `qwen3:0.6b`  
- This is a compact, open-source large language model from Alibaba, suited for local inference.

## Setup Instructions

### 1. Install Ollama

Download and install Ollama from the official site:  
👉 [https://ollama.com/download](https://ollama.com/download)

Once installed, verify it's working:

```bash
ollama --version
````

### 2. Pull the qwen3 Model

Use the following command to download the model:

```bash
ollama pull qwen3:0.6b
```

You can explore other versions with:

```bash
ollama run qwen3
```

### 3. Run the Chatbot Locally

To start a chatbot session with the qwen3 model:

```bash
ollama run qwen3:0.6b
```

You’ll enter a REPL interface where you can chat directly with the model.

### 4. Optional: API Integration

Ollama exposes a local HTTP API at `http://localhost:11434`.

You can make requests like this:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen3:0.6b",
  "prompt": "Hello!",
  "stream": false
}'
```

### 5. Use with Frontend (e.g., Streamlit, Flask)

Run with:

```bash
streamlit run chat.py
```

---

## Troubleshooting

* **Port Conflict**: Ensure no other service is using port 11434.
* **Model Not Found**: If `qwen3:0.6b` isn't available, run `ollama list` to check available models.

## License

This project is for personal/local use. Check qwen3 and Ollama licenses for distribution or commercial usage.
