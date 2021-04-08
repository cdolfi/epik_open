# EPIK Project SMS Sentiment Analysis

## Installation
Before installing, if you can, make a python 3.7 virtual environment and activate it 
(for help see [official docs](https://docs.python.org/3/tutorial/venv.html)).
Then you can run the following command to install all python requirements for the scripts.
```
pip install -r requirements.txt
```
If you have a GPU, you should follow the 
[official pytorch installation instructions](https://pytorch.org/get-started/locally/)
and `pip install` each requirement individually.

## Running Code

### Notebooks
In the `notebooks` folder, you can run the cells of the notebooks in jupyter notebook.
Make sure `jupyter` is installed with `pip install jupyter`.
To run jupyter, run `jupyter notebook` and follow the printed instruction to launch a browser window.

### Scripts

We have some python scripts in this repository that can be run.
First, you need to set your `PYTHONPATH` environment variable to this directory.
On Linux, you can do so with `export PYTHONPATH=$PYTHONPATH:$(pwd)`. 
On Windows, `set "PYTHONPATH=%PYTHONPATH%;%cd%"`.

You can find python scripts in the `scripts` folder.  
For example, to use GoEmotionBert to classify texts, you can run 
```
python scripts/classify_scores.py --model=goemotion-bert --task=emotion --eval-data=data/evaluation_volunteer_text_1000.csv --save-path=data/test.csv
```

## Docker Instructions

We recommend running the scripts and notebooks using Docker.
First, open a terminal window and navigate to the project directory.
From there, you need to build the Docker image by running ```docker build -t <image-name> .```.
You can name the image whatever you like.

Then you can run the image as a Docker container by executing ```docker run -it <image-name> bash```.
This will allow you to access the container in the interactive mode so you can run the scripts and notebooks by using the instructions above.
