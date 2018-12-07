#!/usr/bin/env python
from cmd_parser import make_parser
from io_lists_des import read_input
from Hackathon_2_plot import harry_plotter
from Calculator import output_write

if __name__ == "__main__":
    args = make_parser()
    Samples, ct_mean, ct_sd, standard_means, target = read_input(args.input)
    m, b, r2 = harry_plotter(standard_means)
    output_write(args.output,
                 Samples, ct_mean,
                 args.mean_fragment_length,
                 args.ratio[0]/args.ratio[1],
                 m,b,r2)
