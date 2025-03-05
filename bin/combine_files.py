#!/opt/homebrew/bin/python3

import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Combine all files into one.')
    parser.add_argument('input_dir', help='Input directory to process')
    parser.add_argument('-o', '--output', default='combined.txt', help='Output file name')

    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"Error: {args.input_dir} is not a directory")
        return

    with open(args.output, 'w') as output_file:
        for root, _, files in os.walk(args.input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, args.input_dir)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    output_file.write(f"--- {relative_path} ---\n")
                    output_file.write(content + '\n\n')
                except UnicodeDecodeError:
                    print(f"Skipping binary file: {file_path}")
                except IOError:
                    print(f"Error reading file: {file_path}")

if __name__ == '__main__':
    main()


#  - To run with default output:
#   ```bash
#   python combine_files.py your_input_directory/
#   ```

# - To specify an output file name (optional):
#   ```bash
#   python combine_files.py your_input_directory/ -o combined_output.txt
#   ```
