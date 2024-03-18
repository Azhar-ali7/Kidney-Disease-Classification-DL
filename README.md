# Kidney-Disease-Classification-DL


Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


How to run?
STEPS:

Clone the repository

    https://github.com/Azhar-ali7/Kidney-Disease-Classification-DL

STEP 01- Create a conda environment after opening the repository

    conda create -n cnncls python=3.8 -y

    conda activate cnncls

STEP 02- install the requirements

    pip install -r requirements.txt

# Finally run the following command
    python app.py

Now,

open up you local host and port

MLflow

>[Documentation](https://mlflow.org/docs/latest/index.html)

cmd

    mlflow ui

Dagshub

>[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= https://dagshub.com/Azhar-ali7/Kidney-Disease-Classification-DL.mlflow
MLFLOW_TRACKING_USERNAME= Azhar-ali7
MLFLOW_TRACKING_PASSWORD= 35095490006cce41728e7e378a3cea9d4531e3da
python script.py

Run this to export as env variables:

    export ML_FLOW_TRACKING_URI=https://dagshub.com/Azhar-ali7/Kidney-Disease-Classification-DL.mlflow

    export MLFLOW_TRACKING_USERNAME=Azhar-ali7

    export MLFLOW_TRACKING_PASSWORD=35095490006cce41728e7e378a3cea9d4531e3da
