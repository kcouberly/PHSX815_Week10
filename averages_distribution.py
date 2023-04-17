import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(".")

if __name__ == "__main__":
    
    #default experiments/samples
    M= 500
    samp = 10
    
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            M = Ne            
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            samp = Ns

    #negative parabolic function to use as probability distribution
    def parabolic(x):
        return(x**2)
    para_dis = []
    #loop for single experiment and averages distributions
    averages = []
    for m in range(M):
        #100 random numbers to run through parabolic
        rands = np.random.rand(samp)
        for i in rands:
            para_dis.append(parabolic(i))
        temp = np.asarray(para_dis)
        avg = np.mean(temp)
        averages.append(avg)

#    n, bins, patches = plt.hist(para_dis, bins=25, alpha=0.7 ,rwidth=0.95,density=False, facecolor = "blue")
#    plt.xlabel('value')
#    plt.ylabel('samples')
#    plt.title('x^2 distribution: single experiment ' + str(len(rands)) + ' samples')
#    plt.grid(axis='y', alpha=0.75)
    
#plotting distribution of averages
    n, bins, patches = plt.hist(averages, bins=25, alpha=0.7 ,rwidth=0.95,density=False, facecolor = "blue")
    plt.xlabel('value')
    plt.ylabel('samples')
    plt.title('Averages of ' + str(M) + ' experiments with ' + str(samp) +' samples')
    plt.grid(axis='y', alpha=0.75)


