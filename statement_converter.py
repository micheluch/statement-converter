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