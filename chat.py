import streamlit as st
import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:0.6b"

# Define your prompt template here
SYSTEM_PROMPT = "You are a helpful assistant. Be concise and point to the question. DO NOT include any explanations or reasoning or content within <think></think> tags. If you don't know the answer, say 'I don't know'."

st.title("💬 Chat with Qwen (Ollama)")
st.markdown("Type your message below and hit send to chat with Qwen.")

# Set up initial messages with a system prompt
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hi, how can I help you today?"}
    ]

# Display all chat messages (skip system prompt)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    OLLAMA_API_URL,
                    json={
                        "model": MODEL, 
                        "messages": st.session_state.messages, 
                        "temperature": 0.9,
                        "top_p": 0.95,
                        "top_k": 3,
                        "max_tokens": 512,
                        },
                    stream=True,                    
                )
                response.raise_for_status()

                reply_content = ""
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode("utf-8"))
                        content = data.get("message", {}).get("content", "")
                        reply_content += content

                st.write(reply_content)
                st.session_state.messages.append({"role": "assistant", "content": reply_content})

            except Exception as e:
                error_msg = f"Error: {e}"
                st.write(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
