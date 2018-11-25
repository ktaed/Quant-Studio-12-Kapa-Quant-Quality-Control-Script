#!/usr/bin/python

f = open('MH 3-8_QuantStudio_export.txt','r')
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