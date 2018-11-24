#!/usr/bin/python
import argparse

def make_parser():
    args = argparse.ArgumentParser(description="Quant Studio 12 Kapa Quant Quality Control Script")
    args.add_argument("-i", "--input", help="Path to Input File")
    args.add_argument("-o", "--output", help="Path to Output File")
    args.add_argument("-r", "--ratio", type=int, nargs=2,
                      help="Two Integers to Represent Dilution Factor")
    args.add_argument("-mu", "--mean_fragment_length", type=float,
                      help="Two Integers to Represent Dilution Factor")
    return args.parse_args()

if __name__ == "__main__":
    args = make_parser()
    print(args.input)
    print(args.output)
    print(args.ratio)
    print(args.mean_fragment_length)