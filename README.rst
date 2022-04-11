.. |version| image:: https://img.shields.io/pypi/v/comb-model?style=plastic   :alt: PyPI 
   :target: https://pypi.org/project/comb-model/
   :scale: 100%
.. |license| image:: https://img.shields.io/github/license/lgaalves/combmodel?style=plastic   :alt: GitHub 
   :target:  https://github.com/lgaalves/CombMolde/blob/master/license.rst
   :scale: 100%
.. |downloads| image:: https://img.shields.io/pypi/dm/comb-model?style=plastic    :alt: PyPI - Downloads
   :target: https://pypi.org/project/comb-model/
   :scale: 100%
.. |docs| image:: https://readthedocs.org/projects/comb-model/badge/?version=latest
   :target: https://comb-model.readthedocs.io/?badge=latest
   :alt: Documentation Status
   :scale: 100%



|version| |license| |downloads| |docs| 


comb-model:  A package to simulate Fractional Brownian walks on a comb-like structure.
==========================================================================================

This package simulate trajectories of the comb model via Langevin equations driven by fractional Gaussian noises (long-range correlated).


.. figure:: https://raw.githubusercontent.com/lgaalves/combmodel/main/figures/featured.png
   :height: 489px
   :width: 633px
   :scale: 80 %
   :align: center


Installation
-------------

The ``comb-model`` package is available on pypi and can be installed using pip

.. code-block:: shell

    pip install comb-model

Dependencies
~~~~~~~~~~~~
* ``numpy`` 
* ``stochastic`` 
* ``tdqm`` 

Processes
---------

This package offers functions to simulate Fractional Brownian walks on a plane or Comb-like structures via via Langevin equations.


.. code-block:: python

    # Fractional Brownian walks on a plane
    
    import matplotlib.pyplot as plt
    from combmodel import langevin_fbn
    
    x,y=langevin_fbn(x0=0,y0=0,betax=1,betay=1,hurstx=0.5,hursty=0.5,tmax=1000,disable_tqdm=True)

    
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=(9.1,7))
    ax.plot(x,y,color='#D62728',markersize=0,linewidth=2)
    ax.set_xlabel(r'Position, $x(t)$')
    ax.set_ylabel(r'Position, $y(t)$')

.. figure:: https://raw.githubusercontent.com/lgaalves/combmodel/main/figures/fbm.png
	:height: 489px
	:width: 633px
	:scale: 80 %
	:align: center


.. code-block:: python

	# Fractional Brownian walks on a Comb-like structure

	import matplotlib.pyplot as plt
	from combmodel import comb_model

	x, y = comb_model(x0=0,y0=0,betax=1,betay=1,hurstx=0.5,hursty=0.5,tmax=5000,eps=1,disable_tqdm=True)

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