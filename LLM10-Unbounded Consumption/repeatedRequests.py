import requests
import csv
from concurrent.futures import ThreadPoolExecutor

def query_ollama(prompt, model="qwen2.5:0.5b"):
    url = "http://192.168.154.147:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Change to True for streaming responses
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def process_csv(file_path, model="default", max_workers=5):
    results = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        prompts = [row[0] for row in reader]  # Assuming prompts are in the first column

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda prompt: query_ollama(prompt, model), prompts))

    for prompt, response in zip(prompts, results):
        print(f"Prompt: {prompt}\nResponse: {response}\n")

if __name__ == "__main__":
    model_name = "default"
    csv_file = "prompts.csv"
    max_workers = 4
    process_csv(csv_file, model=model_name, max_workers=max_workers)
