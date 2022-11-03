import pandas as pd
import getopt
import sys

def GetFermi(dos_file):
    file = open(dos_file, 'r')
    for line in file.readlines():
        if line.startswith('# FERMI :'):
            fermi = float(line.strip().split()[-1])
            break
    file.close()
    return fermi

def GetPos(dos_file):
    file = open(dos_file, 'r')
    spin = 0
    pos = {}
    for num, line in enumerate(file.readlines(), 1):
        if "POTENTIAL SPIN DOWN" in line:
            spin = -1
            pos['sd'] = num
        elif "POTENTIAL SPIN UP" in line:
            spin = 1
            pos['su'] = num
        elif "Integrated DOS" in line:
            if spin == 1:
                pos['su_dos' ]= num
            elif spin == -1:
                pos['sd_dos']= num
    file.close()
    return pos

def ExtractData(spin, dos_file, pos):
    file = open(dos_file, 'r')
    content = file.readlines()

    start = pos[spin] + 8
    end   = pos[spin + '_dos'] - 1

    SPINdata=[]
    for line in content[start:end]:
        SPINdata.append(list(filter(None, line.strip().split(' '))))
    file.close()

    SPIN_df = pd.DataFrame(data=SPINdata)


    fermi = GetFermi(dos_file)

    return ( SPIN_df[SPIN_df.columns[0]].astype(dtype = 'float64')-fermi, SPIN_df[SPIN_df.columns[1]].astype(dtype = 'float64'))

