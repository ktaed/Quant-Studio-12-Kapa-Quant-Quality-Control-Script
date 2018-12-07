#!/usr/bin/env python

#This should probably be made a function eventually that takes arguments for slope, Yint, frag length, and dilution factor

def output_write(output_file_name, samples, ct_mean, mu_frag, dil_factor, m,b,r2 ):
    def Concentration_pM(d_factor, ct, Yint, slope, frag):
        return (d_factor * (10 ** ((float(ct) - Yint) / float(slope))) * (452 / float(frag)))
        # return result

    def Concentration_uguL(concentration_pM, frag):
        return ((concentration_pM) * (10 ** -15) * frag * 617.9 * 10 ** 6)

    OutFile = open(output_file_name, 'w')
   #Header for output file
    OutFile.write('Sample Name\tConcentration of undiluted library(pM)\tConcentration of undiluted library (nM)\tConcentration of undiluted library(ug/uL)\n')
    for i, samp in enumerate(samples):
        temp = Concentration_pM(dil_factor,ct_mean[i], b,m,mu_frag)
        OutFile.write("{}\t{}\t{}\t{}\n".format(samp,temp,temp/1000,Concentration_uguL(temp,mu_frag) ))

    OutFile.write("\nR^2={}\nSlope={}\nYint={}\n".format(r2,m,b))
    OutFile.close()
