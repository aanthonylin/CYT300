#!/bin/bash

# Check for required arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <target_url> <payload_directory>"
    exit 1
fi

TARGET_URL="$1"
PAYLOAD_DIR="$2"
OUTPUT_FILE="fuzz_results.txt"

# Check if wfuzz is installed
if ! command -v wfuzz &> /dev/null; then
    echo "Error: wfuzz is not installed. Install it with: sudo apt install wfuzz"
    exit 1
fi

# Check if the directory exists
if [ ! -d "$PAYLOAD_DIR" ]; then
    echo "Error: Directory '$PAYLOAD_DIR' not found."
    exit 1
fi

# Clear previous output file
> "$OUTPUT_FILE"

# Iterate over payload files and run wfuzz for each
for payload_file in "$PAYLOAD_DIR"/*; do
    echo "[+] Testing with payload file: $payload_file" | tee -a "$OUTPUT_FILE"
    wfuzz -w "$payload_file" "$TARGET_URL/FUZZ" -c | tee -a "$OUTPUT_FILE"
    echo "--------------------------------------------" | tee -a "$OUTPUT_FILE"
done

echo "[+] Fuzzing complete. Results saved in $OUTPUT_FILE"