#!/usr/bin/python
def read_input(file_name):
    f = open(file_name,'r')
    lines = f.readlines()[46:430]
    f.close()

    Samples = []
    ct_mean = []
    ct_sd = []

    for i in lines:
        samples = []
        cm = []
        cs = []
        samples.append(i.split('\t')[3])
        for x in samples:
            if x != 'empty':
                Samples.append(x)
        cm.append(i.split('\t')[9])
        for x in cm:
            if x != '':
                ct_mean.append(x)
        cs.append(i.split('\t')[10])
        for x in cs:
            if x != '':
                ct_sd.append(x)

    #del(lines)

    Samples = sorted(set(Samples), key=lambda x: Samples.index(x))
    ct_mean = sorted(set(ct_mean), key=lambda x: ct_mean.index(x))
    ct_sd = sorted(set(ct_sd), key=lambda x: ct_sd.index(x))
    standard_means = ct_mean[-7:-1]
    target = ct_mean[0:-8]
    target.append(ct_mean[24])
    return Samples, ct_mean, ct_sd, standard_means, target
    

Samples, ct_mean, ct_sd, standard_means, target = read_input("MH 3-8_QuantStudio_export.txt")
