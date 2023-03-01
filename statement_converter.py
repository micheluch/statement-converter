import csv

def line_to_csv(line: str):
    return '|'.join(split_line(line))

def split_line(line: str):
    results = []
    segments = line.split()
    results.append(segments[0])
    results.append(' '.join(segments[1:-1]))
    results.append(segments[-1])
    return results

def convert_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        with open(output_file_path, 'w') as w:
            lines = []
            for line in f:
                line = line_to_csv(line)
                lines.append(line + '\n')
            lines[-1] = lines[-1].rstrip()
            w.writelines(lines)

def main(input_file_path, output_file_path):
    convert_file(input_file_path=input_file_path, output_file_path=output_file_path)
    #print("Input file path:  " + input_file_path)
    #print("Output file path: " + output_file_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Chase statement files to csv")
    parser.add_argument('input_file_path')
    parser.add_argument('output_file_path')
    args = parser.parse_args()
    main(input_file_path=args.input_file_path, output_file_path=args.output_file_path)