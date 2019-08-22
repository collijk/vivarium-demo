============================================================
Intro to Simulation with Vivarium and Vivarium Public Health
============================================================

These two presentations give an introduction to public health simulations using
vivarium.  

Part I gives an overview of the field of computational simulation and
a bit of background on the start of the Vivarium project.  It then gives an explanation
of individual-based, discrete-time, Monte Carlo simulation; the methodology used
for most Vivarium simulation projects. Finally, it talks about the models and 
implementations we've put together in Vivarium Public Health, our toolbox
for public health and intervention modeling.

Part II recaps the modeling methodology and then explores the concept model
diagram and its correspondence to modeling components in a bit more depth.

Videos of these presentations can be found on youtube.

- `Part I <https://www.youtube.com/watch?v=SAqX6NHpk1A&feature=youtu.be>`_
- `Part II <https://youtu.be/rTiJTTaEb-g>`_


Installation Instructions
-------------------------

You will need ``git``, ``git-lfs`` and ``conda`` to get this repository 
and install all of it's requirements.  You should follow the instructions for 
your  operating system at the following places:

- `git <https://git-scm.com/downloads>`_
- `git-lfs <https://git-lfs.github.com/>`_
- `conda <https://docs.conda.io/en/latest/miniconda.html>`_

Once you have all three installed, you should open up your normal shell 
(if you're on linux or OSX) or the ``git bash`` shell if your on windows.  
You'll then make an environment, clone this repository, then install
all necessary requirements as follows::

  $> conda create --name=vivarium-demo python=3.6
  ...conda will download python and base dependencies...
  $> conda activate vivarium-demo
  (vivarium-demo) $> git clone https://github.com/collijk/vivarium-demo.git
  ...git will copy the repository from github and place it in your current directory...
  (vivarium-demo) $> cd vivarium-demo/2019_07_25_ihme
  (vivarium-demo) $> pip install -r requirements.txt
  ...pip will install vivarium and other requirements...
  
Cloning the repository should take a fair bit of time as git must fetch
the data artifact associated with the demo (about .5GB of data) from the 
large file system storage (``git-lfs``).  If your clone works quickly, 
you are likely only retrieving the checksum file that github holds onto, 
and your simulations will fail.
  
The ``(vivarium-demo)`` that precedes your shell prompt will probably show
up by default, though it may not.  It's just a visual reminder that you
are installing and running things in an isolated programming environment
so it doesn't conflict with other source code and libraries on your 
system.


Running the Notebook
--------------------

Once you have everything installed, you can launch the notebook with the
the presentation with jupyter.  With the ``vivarium-demo`` environment
active, navigate to the directory with the ``population_health_modeling.ipynb``
in it and run::

  (vivarium-demo) $> jupyter notebook
  
This will open up a landing page with a directory tree where you can open
the notebook.  This is an active code environment, so you can excecute all
of the code cells present as well as add new code if you want to explore.

You can find more information about working with jupyter notebooks at their
documentation.

- `Jupyter docs <https://jupyter-notebook.readthedocs.io/en/stable/>`_
