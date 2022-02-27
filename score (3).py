import joblib
import json
import numpy as np
import os
import math


from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType

def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # For multiple models, it points to the folder containing all deployed models (./azureml-models)
    #model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    # Deserialize the model file back into a sklearn model.
    model = joblib.load(model_path)

def run(data):
   try:
     data = json.loads(data)
     result = model.predict(data['data'])
     return {'data' : result.tolist() , 'message' : "Successfully clustered the patient into a survival group"}
   except Exception as e:
      error = str(e)
      return {'data' : error , 'message' : 'Failed to cluster patient'}
    
