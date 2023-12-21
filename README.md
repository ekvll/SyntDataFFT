# SyntDataFFT README

- [Introduction](#introduction)
- [Usage](#usage)
  - [Run SyntDataFFT](#run-syntdatafft)
    - [Through Terminal](#through-terminal)
    - [As an Executable file](#as-an-executable-file)
  - [User-defined parameters](#user-defined-parameters)
    - [Signal parameters](#signal-parameters)
    - [Anomaly parameters](#anomaly-parameters)
  - [Compute fast Fourier transform and plot the result](#compute-fast-fourier-transform-and-plot-the-result)
- [Build](#build)
  - [Create a Local Python Package](#create-a-local-python-package)
  - [Create an Executable File](#create-an-executable-file-1)
- [Tests](#tests)
- [Contribute](#contribute)

## Introduction

SyntDataFFT is a tool designed to generate synthetic raw signals based on user-defined input parameters. This application is particularly useful for mimicking accelerometer data along a 1D profile, allowing users to simulate signals containing up to two anomalies. The anomalies are represented as geometrical irregularities within the signal, providing a valuable testing ground for various applications.

After generating the synthetic raw signal, SyntDataFFT applies a Hamming window to the signal and computes the Numpy fast Fourier transform (FFT) of the windowed signal. The resulting raw signal, windowed signal, and frequency spectrum of the windowed signal are visualized in plots for easy analysis.

## Usage

### Run SyntDataFFT

#### Through Terminal
First, clone the SyntDataFFT repository. Open a terminal and navigate to where you want to locally store the clone, and then run the following command:
```
git clone https://github.com/ekvll/SyntDataFFT
```
Now, navigate to the project root, typically by:
```
cd ./SyntDataFFT
```
To run the application through Python, execute:
```
python main.py
```

#### As an Executable file
Download SyntDataFFT as an executable (.exe) file [here](https://nppd.se/syntdatafft/index.html), and double-click on the .exe file.

### User-defined parameters

Upon application start, default values for signal and anomaly parameters are utilized. Customize the parameters according to your requirements.

* __Signal parameters__
    * __Signal duration (s)__ - Length of raw signal in seconds.
    * __Sampling rate (Hz)__ - Sampling rate of raw signal in Hertz.
    * __Noise level__ - Amplitude of normally distributed noise added to raw signal.

* __Anomaly parameters__
    * __Amplitude__ - Initial anomaly amplitude. 
    * __Start time (s)__ - Moment in time, in seconds, when anomaly is initialized.
    * __Duration (s)__ - Duration of anomaly in seconds.
    * __Frequency (Hz)__ - Frequency of anomaly in Hertz.
    * __Exponential decay__ - Magnitude of exponential decay applied to anomaly at anomaly initialization.


### Compute fast Fourier transform and plot the result

To compute the FFT of the raw signal and visualize the plots, press the ```Update plot``` button.

Feel free to explore and experiment with different parameter settings to generate and analyze synthetic signals effectively.

![Alt text](img/syntdatafft.png)

## Build

### Create a Local Python Package

To build a local Python package for SyntDataFFT, open a terminal, navigate to the project root, and run the following command:
```
python setup.py sdist
```

### Create an Executable File

First, make sure you have PyInstaller installed in your environment.
Through conda, run:
```
conda install -c conda-forge pyinstaller
```
Through pip, run:
```
pip install pyinstaller
```

Build the executable (.exe) file for SyntDataFFT using PyInstaller. Open a terminal, navigate to the project root, and run the following command:
```
pyinstaller SyntDataFFT.spec
```

## Tests

Execute implemented tests using pytest by opening a terminal, navigating to the project root, and running:
```
pytest
```

## Contribute

To contribute to SyntDataFFT, do the following:

### 1. Start an Issue
Start an issue in the SyntDataFFT reporistory. State what you are planning to work on. Take note of the issue number, as we later on are going to reference to the issue.
### 2. Fork the SyntDataFFT repository
Click the "Fork" button to create a copy of the SyntDataFFT repository on your GitHub account.
### 3. Clone your fork
On your forked repository, click "Code" and copy the URL. Then, open a terminal and navigate to where you want to store the local copy of the SyntDataFFT repository. In the terminal, run the following:
```
git clone <forked-repository-url>
```
### 4. Create a new branch
Create a new branch for your contribution:
```
git checkout -b <your-branch-name>
```
### 5. Make your changes
### 6. Commit changed
Stage changes:
```
git add .
```
Commit the changes:
```
git commit -m "<fix #issue-number: description of changes>"
``` 
### 7. Push changes to your fork
Push your changes to your forked version of the SyntDataFFT GitHub repository:
```
git push origin <your-branch-name>
```
### 8. Create pull-request
Visit your forked repository on GitHub. Click the "New pull request" button. Write a title and comment (include issue number in the comment) for your pull request. Click "Create pull request" button.
