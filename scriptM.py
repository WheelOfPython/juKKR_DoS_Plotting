from script_cwd import *
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

# Order of line colors 
clrlst = [
(0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
(1.0, 0.4980392156862745, 0.054901960784313725),
(0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
(0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
(0.5803921568627451, 0.403921568627451, 0.7411764705882353),
(0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
(0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
(0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
(0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
(0.09019607843137255, 0.7450980392156863, 0.8117647058823529)]

##############################################################################

def Plotting(dos_file, clrnum):
    pos = GetPos(dos_file)
    
    SU_data = ExtractData('su', dos_file, pos)
    SD_data = ExtractData('sd', dos_file, pos)
    
    clr = clrlst[clrnum-1 % len(clrlst)]
    plt.plot(SU_data[0], SU_data[1], linewidth=1, color=clr)
    plt.plot(SD_data[0], SD_data[1], linewidth=1, color=clr)

##############################################################################

def mainmain():
    first = 1
    last  = 1
    title = 'DoS'
    save  = 0
    
    argv = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "s:e:t:o:")
    except:
        print("Parsing Error")
  
    for opt, arg in opts:
        if opt in ['-s']:
            first = arg
        elif opt in ['-e']:
            last = arg
        elif opt in ['-t']:
            title = arg
        elif opt in ['-o']:
            save = arg
    
    for i in range(int(first), int(last)+1):
        Plotting('dos.atom' + str(i), i)

    plt.title(title + ' [Ef: '+ str(GetFermi('dos.atom1'))+' Ry]')
    plt.xlabel('Energy (Ry)')
    plt.ylabel('n(E)')
    plt.axhline(y=0, color='grey', linestyle='dashed', linewidth=1)
    plt.axvline(x=0, color='r'   , linestyle='dashed', linewidth=1.5)
    
    if save:
        plt.savefig(title + '.svg', format='svg', dpi=1200)
    
    plt.show()

##############################################################################

if __name__ == "__main__":
    mainmain()
