zaproxy -cmd -quickurl https://192.168.154.156 > ZAP_scan.txt
promptfoo redteam run
conda activate garak_env
garak --model_type ollama --model_name qwen-with-mitigations --probes lmrc.Profanity
garak --model_type ollama --model_name qwen-with-mitigations --probes encoding.InjectBase32
garak --model_type ollama --model_name qwen-with-mitigations --probes realtoxicityprompts.RTPIdentity_Attack
python llmguard.py
