# END to END prediction project


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## Deployment
Website(Azure):```
 https://winequalityprediction.azurewebsites.net/  
  ```
# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Asazin007/Prediction_project.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.9 -y
```

```bash
conda activate venv/
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Asazin007/Prediction_project.mlflow \
MLFLOW_TRACKING_USERNAME=Asazin007 \
MLFLOW_TRACKING_PASSWORD=208a3bd1db392b67e9aabffa34a9b3676091ee96 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Asazin007/Prediction_project.mlflow

export MLFLOW_TRACKING_USERNAME=Asazin007 

export MLFLOW_TRACKING_PASSWORD=208a3bd1db392b67e9aabffa34a9b3676091ee96

```


## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

