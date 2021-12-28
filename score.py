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
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    # Deserialize the model file back into a sklearn model.
    model = joblib.load(model_path)
    

input_sample = np.array([[6133,74.6,0,5.0,2.0,0,0.0,7.0,3.078,0,0,39.0,1,2,0,2,1,1,2,0,1,0,3,1,2,0,0,0]])
output_sample = np.array([3])
@input_schema('X_train', NumpyParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(X_train):
    try:
        result =model.predict(X_train)
        # You can return any JSON-serializable object.
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error 