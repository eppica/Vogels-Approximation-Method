# :chart_with_upwards_trend: Vogel's Approximation Method

## About

This project aims to solve a [Transport Problem](https://github.com/eppica/Vogels-Approximation-Method/wiki#the-transport-problem) for the Linear Programming class using an algorithm that implements the Vogel's Approximation method.

## Technologies

- [Python](https://www.python.org)


## Requirements

To run and edit the project, be sure to have installed in your computer the following softwares:

- [Python](https://www.python.org/downloads/)
- A code editor

After that, you'll need to clone this repo:

```
git clone https://github.com/eppica/Vogels-Approximation-Method.git
```

## Setup

Inside the project directory, [create a virtual environment](https://docs.python.org/3/library/venv.html) (venv)

At the ```cmd```, type:

```
python -m venv ./venv
```

After that you should see a venv directory.

To run commands using venv, go to ```Scripts``` directory inside ```venv```:
```
Vogels-Approximation-Method
│   main.py
│   ...
└─── 🗀 venv
     └─── 🗀 Scripts
          │   activate
```
To use the virtual environment, run:

```
activate
```
Then, using the virtual environment, install the project requirements:

```
pip install -r requirements.txt
```

That will prevent you to install the libs in the local computer, and it will be available only on the project scope.  

## Editing

Whenever you install a new library, you need to update the ```requirements.txt``` file.

At the ```cmd```, run:
```
pip freeze > requirements.txt
```
## Running

### venv:
To see the project running, inside the virtual environment at ```cmd```, run:
```
python main.py
```

## :balance_scale: License

[MIT License](https://github.com/eppica/Vogels-Approximation-Method/blob/main/LICENSE)
