import csv
import argparse

def line_to_csv(line: str):
    return ','.join(split_line(line))

def split_line(line: str):
    results = []
    segments = line.split()
    results.append(segments[0])
    results.append(''.join(segments[1:-2]))
    results.append(segments[-1])
    return results

def convert_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        with open(output_file_path, 'w') as w:
            lines = []
            for line in f:
                lines.append(line)
                print(line)
            w.writelines(lines)
    with open(output_file_path, "r") as f:
        for line in f:
            print(line)