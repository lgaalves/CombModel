import numpy as np
from tqdm import tqdm

import os
import sys  
from stochastic.processes.noise import FractionalGaussianNoise

def generate_noise(hurstx,hursty,tmax):
    """
    Generate sequences of fractional Gaussian noise. 

    Parameters
    ----------
    hurstx: float
        Hurst exponent in the x-direction. Vales must be in the range (0,1). 
    hursty: float
        Hurst exponent in the y-direction. Vales must be in the range (0,1). 
    tmax: int
        Maximum number of time-step simulated.

    Returns
    -------
    noisex: np.array
       Simulated noise in the x-axis.
    noisey: np.array
       Simulated noise in the y-axis.

    Examples
    --------
    >>> generate_noise(hurstx=0.5,hursty=0.5,tmax=5)
    (array([ 0.25768888,  0.26578568, -0.5264168 , -0.22897338,  1.5653223 ]),
     array([ 0.07702825, -0.76531544,  1.30514932, -1.88840645,  0.12964754]))

    >>> generate_noise(hurstx=0.05,hursty=0.99,tmax=5)
    (array([ 0.86985584, -0.06461844, -1.14352549, -0.58317815, -1.46406803]),
    array([-1.70277230e-01, -3.01093568e-01, -3.67460604e-01,  2.79234304e-04,-1.12502245e-01]))
    """
    fgn = FractionalGaussianNoise(hurst=hurstx, t=tmax)
    noisex = np.array(fgn.sample(tmax,algorithm='hosking'))
    fgn = FractionalGaussianNoise(hurst=hursty, t=tmax)
    noisey = np.array(fgn.sample(tmax,algorithm='hosking'))
    return noisex,noisey

def langevin_fbn(x0,y0,betax,betay,hurstx,hursty,tmax,disable_tqdm=False):
    """
    Compute fractional Brownian motion trajectory. 

    Parameters
    ----------
    x0: float
        Initial position in the x-axis.
    y0: float
        Initial position in the y-axis.
    betax: float
        Constant related to diffusion coefficient in the x-direction. 
    betay: float
        Constant related to diffusion coefficient in the y-direction.
    hurstx: float
        Hurst exponent in the x-direction. Vales must be in the range (0,1). 
    hursty: float
        Hurst exponent in the y-direction. Vales must be in the range (0,1). 
    tmax: int
        Maximum number of time-step simulated.
    disable_tqdm: boolean
        If `False`, shows progressbar. If `True` disable progressbar.

    Returns
    -------
    x: np.array
       Simulated positions in the x-axis.
    y: np.array
       Simulated positions in the y-axis.

    Examples
    --------

    >>> langevin_fbn(x0=0,y0=0,betax=1,betay=1,hurstx=0.5,hursty=0.5,tmax=10,disable_tqdm=False)
    100%|███████████████████████████████████████████████████████████████| 9/9 [00:00<00:00, 219469.40it/s]
    (array([ 0.        ,  0.31802743, -0.83832619, -0.27312321,  0.04191725,
             0.23666782, -1.75041569, -0.14763177, -0.50695669,  0.152747  ]),
     array([ 0.        , -1.33455269, -0.76376196,  0.10190015,  0.54170037,
             1.03303179, -0.310934  ,  0.92504652,  1.77317527,  0.68204445]))

    >>> langevin_fbn(x0=0,y0=0,betax=1,betay=1,hurstx=0.05,hursty=0.95,tmax=10,disable_tqdm=True)
    (array([ 0.        , -1.06714954, -2.42275827, -2.15268094, -1.94348332,
        -2.83243755, -3.12425033, -3.72050659, -2.4537888 , -1.05256446]),
     array([ 0.        , -1.65366648, -3.24551102, -2.65525154, -3.31656122,
            -2.50457923, -2.05895687, -0.73025872, -0.64509908, -0.09122725])))

    """
    x,y=np.zeros(tmax),np.zeros(tmax)
    x[0],y[0]=x0,y0

    noisex,noisey=generate_noise(hurstx,hursty,tmax)
    for t in tqdm(range(0,tmax-1),disable=disable_tqdm):
        x[t+1]=x[t]+betax*noisex[t]
        y[t+1]=y[t]+betay*noisey[t]
    return x,y

def comb_model(x0,y0,betax,betay,hurstx,hursty,tmax,eps,disable_tqdm=False):
    """
    Compute Comb-model trajectory using fractional Brownian noise. 

    Parameters
    ----------
    x0: float
        Initial position in the x-axis.
    y0: float
        Initial position in the y-axis.
    betax: float
        Constant related to diffusion coefficient in the x-direction. 
    betay: float
        Constant related to diffusion coefficient in the y-direction.
    hurstx: float
        Hurst exponent in the x-direction. Vales must be in the range (0,1). 
    hursty: float
        Hurst exponent in the y-direction. Vales must be in the range (0,1). 
    tmax: int
        Maximum number of time-step simulated.
    eps: float
        Width of band where movement in the x-direction is allowed. 
    disable_tqdm: boolean
        If `False`, shows progressbar. If `True` disable progressbar.

    Returns
    -------
    x: np.array
       Simulated positions in the x-axis.
    y: np.array
       Simulated positions in the y-axis.

    Examples
    --------
    >>> comb_model(x0=0,y0=0,betax=0.1,betay=0.1,hurstx=0.5,hursty=0.5,tmax=10,eps=0.1,disable_tqdm=False)
    100%|███████████████████████████████████████████████████████████████| 9/9 [00:00<00:00, 142987.64it/s]
    (array([ 0.        ,  0.06893574, -0.18618081, -0.16402136, -0.08273242,
            -0.10966074, -0.10966074, -0.08535346, -0.05060382,  0.03196749]),
     array([ 0.        , -0.07952973, -0.0537798 , -0.02380105,  0.0382455 ,
             0.10637735, -0.05516008,  0.02736965,  0.04563519,  0.16306934]))

    >>> comb_model(x0=0,y0=0,betax=1,betay=1,hurstx=0.5,hursty=0.99,tmax=10,eps=1,disable_tqdm=True)
    (array([ 0.        , -1.68859052, -1.77776905, -2.71815718, -2.35059768,
        -2.35059768, -2.35059768, -2.35059768, -2.35059768, -2.35059768]),
     array([ 0.        , -0.59174592, -0.69523766,  0.30401518,  1.20541352,
             2.86754674,  3.40154263,  3.12629311,  2.44392253,  0.86665015]))
    """
    x,y=np.zeros(tmax),np.zeros(tmax)
    x[0]=x0
    y[0]=y0
    noisex,noisey=generate_noise(hurstx,hursty,tmax)
    for t in tqdm(range(0,tmax-1),disable=disable_tqdm):
        if np.abs(y[t])<=eps:
            x[t+1]=x[t]+betax*noisex[t]
            y[t+1]=y[t]+betay*noisey[t]
        else:
            x[t+1]=x[t]
            y[t+1]=y[t]+betay*noisey[t]

    return x,y

