combmodel:  A package to simulate Fractional Brownian walks on a comb-like structure.
==========================================================================================

This package simulate trajectories of the comb model via Langevin equations driven by fractional Gaussian noises (long-range correlated).


.. figure:: https://raw.githubusercontent.com/lgaalves/combmodel/figures/featured.png
   :height: 489px
   :width: 633px
   :scale: 80 %
   :align: center


Installation
-------------

The ``combmodel`` package is available on pypi and can be installed using pip

.. code-block:: shell

    pip install combmodel

Dependencies
~~~~~~~~~~~~
* ``numpy`` 
* ``stochastic`` 
* ``tdqm`` 

Processes
---------

This package offers functions to simulate Fractional Brownian walks on a plane or Comb-like structures via via Langevin equations.



Fractional Brownian walks on a plane

	.. code-block:: python
		import matplotlib.pyplot as plt
		from combmodel import langevin_fbn
		x,y=langevin_fbn(0,0,0.1,0.1,0.5,0.5,10**3,disable_tqdm=True)
		f, ax = plt.subplots(nrows=1, ncols=1, figsize=(9.1,7))
		ax.plot(x,y,color='#D62728',markersize=0,linewidth=2)
		ax.set_xlabel(r'Position, $x(t)$')
		ax.set_ylabel(r'Position, $y(t)$')

	.. figure:: https://raw.githubusercontent.com/lgaalves/combmodel/main/figures/fbm.png
	   :height: 489px
	   :width: 633px
	   :scale: 80 %
	   :align: center

Fractional Brownian walks on a Comb-like structure

	.. code-block:: python
		import matplotlib.pyplot as plt
		from combmodel import comb_model
		x, y = comb_model(x0=0,y0=0,betax=1,betay=1,hurstx=0.5,hursty=0.5,tmax=5000,eps=1,disable_tqdm=False)
		f, ax = plt.subplots(nrows=1, ncols=1, figsize=(9.1,7))
		ax.plot(x,y,color='#D62728',markersize=0,linewidth=2)
		ax.set_xlabel(r'Position, $x(t)$')
		ax.set_ylabel(r'Position, $y(t)$')

	.. figure:: https://raw.githubusercontent.com/lgaalves/combmodel/main/figures/comb.png
	   :height: 489px
	   :width: 633px
	   :scale: 80 %
	   :align: center

References
==========

.. [#ribeiro2014] Haroldo V. Ribeiro, Angel A. Tateishi, Luiz G. A. Alves, Rafael S. Zola, Ervin K Lenzi (2014). Investigating the interplay between mechanisms of anomalous diffusion via fractional Brownian walks on a comb-like structure. DOI: http://dx.doi.org/10.1088/1367-2630/16/9/093050