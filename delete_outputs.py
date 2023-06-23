import os
import nbformat as nbf
from nbconvert.preprocessors import ClearOutputPreprocessor

# Get the current working directory
notebook_dir = os.getcwd()

# Create a preprocessor
c = ClearOutputPreprocessor()

for file_name in os.listdir(notebook_dir):
    if file_name.endswith(".ipynb"):
        # Open the notebook
        with open(os.path.join(notebook_dir, file_name), 'r') as f:
            nb = nbf.read(f, nbf.NO_CONVERT)

        # Clear the outputs
        c.preprocess(nb, {})

        # Save the notebook
        with open(os.path.join(notebook_dir, file_name), 'w') as f:
            nbf.write(nb, f)