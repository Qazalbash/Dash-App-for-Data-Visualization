# Dash App for Data Visualization
[![Total alerts](https://img.shields.io/lgtm/alerts/g/MeesumAliQazalbash/Dash-App-for-Data-Visualization.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MeesumAliQazalbash/Dash-App-for-Data-Visualization/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MeesumAliQazalbash/Dash-App-for-Data-Visualization.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MeesumAliQazalbash/Dash-App-for-Data-Visualization/context:python)


The app is a dashboard which is utilized in visualizing the COVID-19 data of the USA from January 2020 to April 2022. It is made with the help of plotly and dash - popular python modules for interactive graphs.

## Requirement

### Create a virtual enviorment (Optional)

To make virtual enviornment first install the `virtualenv` module of python by,

```console
pip install virtualenv
```

Open terminal in the current working directory and write,

```console
virtualenv <enviornment name>
```

Activate the enviornment by running the following command in the very same working directory.

```console
source <enviornment name>/bin/activate
```

First install the required modules by running the following command in the terminal of the directory.

```console
pip install -r requirement.txt
```

or run these commands in the terminal

```console
pip install pathlib
pip install pandas=1.4.2
pip install numpy=1.22.3
pip install dash=2.4.1
pip install plotly=5.8.0
```

## How to run?

Run the following command in the terminal

```console
python app.py
```

After this a local host link will appear in the terminal, that would look like this,

`http://127.0.0.1:8050/`

Open this link in browser and play with the maps.
