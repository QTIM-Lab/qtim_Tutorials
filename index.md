# Welcome to QTIM Tutorials!

The purpose of these tutorials is to provide a broad overview of techniques for applying machine learning to medical images. Specifically, we focus on building a set of skills to make you an effective machine learning practioner with a good understanding of the underlying theory:

- Python programming: variables, types, data structures, control flow, I/O
- Project management: data organization, modular code design, version control
- Data science: tabular data, feature selection, normalization, plotting
- Image processing: images as arrays, multi-dimensional data, thresholding, morphological operations
- Machine learning models: decision trees, random forests, support vector machines, logistic regression, multi-layer perceptrons
- Deep learning: convolutional neural networks, image classification, image segmentation, interpretability of features

## Requirements

The tutorials are designed such that anyone with an interest in applying ML to medical images can follow along, regardless of programming experience. However, the following prior experience would be useful:

- Rudimentary programming skills in a high-level language, such as Python or MATLAB
- Using the terminal to navigate your computer's file system and run simple commands
- A basic understanding of linear algebra, particularly operations between scalars, vectors and matrices
- Familiarity with basic image processing techniques

## Getting started
All of our tutorials are written in Python 3 as Jupyter Notebooks. To get started, follow the installation steps below:

1. Download and install Python 3.6 (or greater). We highly recommend [Anaconda](https://www.anaconda.com/download/), which includes many of the dependencies you'll need (including Jupyter). The process will vary depending on platform, but is usually straightfoward.
2. Download the tutorial notebooks from [here](https://github.com/QTIM-Lab/qtim_Tutorials). We highly recommend using  Git, as the tutorials will be updated as time goes on. If you're unfamilar with git, just download and unpack the code as a [zip file](https://github.com/QTIM-Lab/qtim_Tutorials/archive/master.zip).
3. In a terminal, install the following additional dependencies using `pip` (comes with Anaconda):
   * `pip install tensorflow`
   * `pip install keras`
  
## Running a tutorial
1. In a terminal, navigate to the *qtim_Tutorials* folder you cloned/unzipped in step 2 above.
2. Run the command `jupyter notebook`. A new browser window/tab should appear.
3. Click on the tutorial folder you want to run, and then click the *.ipynb* file in that folder.
4. To run a chunk of code, click in a box and hit Ctrl + Enter (or the 'Run' button in the top panel).

That's it! If you happen to hit errors, then consider the following:
* Code blocks must be run in order from top to bottom, as they often rely on each other. Be sure to go back and check all preceding blocks have been run.
* The `[*]` beside a code block indicates that the code is currently running. You'll need to wait until it finishes before moving on.
* Be sure to read the descriptions as you go; some steps involve downloading external data.
* File paths can be confusing for first-time coders. The easiest solution is to put any download data in the same folder as the tutorial you're running; that way you can reference the data by folder name, rather than */lots/of/nested/directories/...*
* If all else fails, [Stack Overflow](https://stackoverflow.com/search?q=) is your friend :)
