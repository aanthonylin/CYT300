import subprocess
import csv
from concurrent.futures import ThreadPoolExecutor
import json

def query_ollama(prompt, model="qwen2.5:0.5b"):
    url = "http://192.168.154.155:11434/api/generate"
    payload = "{\"model\":\""+model+"\",\"prompt\":\""+prompt+"\",\"stream\": false}"
    try:
        result = subprocess.run(
            ["curl", "-X", "POST", url, "-H", "Content-Type: application/json", "-d", payload],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"
        data = json.loads(result.stdout)
        return data.get("response", "No response received.")
    except Exception as e:
        return f"Error: {e}"

def process_csv(file_path, model="qwen2.5:0.5b", max_workers=4):
    results = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        prompts = [row[0] for row in reader]  # Assuming prompts are in the first column

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda prompt: query_ollama(prompt, model), prompts))

    for prompt, response in zip(prompts, results):
        print(f"Prompt: {prompt}\nResponse: {response}\n")

if __name__ == "__main__":
    csv_file = "sample_prompts.csv"
    max_workers = 10
    process_csv(csv_file, max_workers=max_workers)
