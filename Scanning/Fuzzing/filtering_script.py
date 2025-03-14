def filter_response_codes(input_file, output_file, codes_to_remove):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not any(f" {code} " in line for code in codes_to_remove):
                outfile.write(line)

if __name__ == "__main__":
    input_file = "8080_fuzz_results.txt"  # Change this if needed
    output_file = "filtered_results.txt"

    # Specify response codes to remove (e.g., 200, 404, 500)
    codes_to_remove = ["200", "404"]

    filter_response_codes(input_file, output_file, codes_to_remove)
    print(f"Filtered results saved to {output_file}")