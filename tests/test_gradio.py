import os
import gradio as gr
import aiohttp
from dotenv import load_dotenv

# Initialize environment variables
load_dotenv()

# Initialize backend & API keys
server_api_key = os.environ['BACKEND_API_KEY']

async def call_gpt_api(user_id, query, user_locale):
    url = "http://127.0.0.1:8800/gpt"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {server_api_key}"
    }
    payload = {
        "user_input": query,
        "user_locale": user_locale,
        "user_id": user_id,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json() 
                return data.get('output', 'No output in response')
            else:
                return f"Error: {response.status} - {await response.text()}"

def setup_gradio():
    with gr.Blocks() as app:
        with gr.Row():
            user_id_input = gr.Textbox(label="Enter your User ID", placeholder="e.g., 8811")
            query_input = gr.Textbox(label="Enter your query", placeholder="Type here...")
            locale_input = gr.Textbox(label="Locale", placeholder="e.g., eng", value="eng")
            submit_btn = gr.Button("Submit")
        output_area = gr.Textbox(label="Output")
        
        submit_btn.click(call_gpt_api, inputs=[user_id_input, query_input, locale_input], outputs=output_area)
        
    app.launch(share=True)

if __name__ == "__main__":
    setup_gradio()
