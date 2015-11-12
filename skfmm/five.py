import numpy as np
import pylab as plt
import matplotlib.patches as patches
from sys import float_info
from bi_cubic_init import BiCubicInit


def plot_array(arr, extra=None):
    plt.matshow(arr)
    plt.gca().add_patch(patches.Circle((0,0), 3, fill=False))
    plt.gca().set_xticks([x-0.5 for x in plt.gca().get_xticks()][1:],
                         minor='true')
    plt.gca().set_yticks([y-0.5 for y in plt.gca().get_yticks()][1:],
                         minor='true')
    plt.grid(which='minor')
    plt.colorbar()
    for i in range(6):
        for j in range(6):
            if hasattr(arr, "mask"):
                if not arr.mask[i,j]:
                    plt.text(i,j,"{:.02e}".format(arr[i,j]))
            else:
                plt.text(i,j,"{:.02e}".format(arr[i,j]))
    if extra and hasattr(extra,'__call__'):
        extra()

    plt.show()


x, h= np.linspace(0,5,6,retstep=True)

X,Y = np.meshgrid(x,x)

phi = X**2 + Y**2 - 3**2

#plot_array(phi)
a=BiCubicInit(phi, 1)


#plot_array(a.aborders)

arr=np.copy(a.d)
mask = arr==float_info.max
bb=np.ma.MaskedArray(arr,mask)
bb[phi<0] *= -1

def my_extra():
    for k,v in a.pdict.iteritems():
        plt.plot((k[0], k[0]+v[0]), (k[1], k[1]+v[1]), "-o")

plot_array(bb, my_extra)