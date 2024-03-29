# entity here first we'll do it later in entity folder

from pathlib import Path
from dataclasses import dataclass

# dataclass is a decorator 
# Dataclasses are a way to make Python classes easier and simpler.
# Classes are like blueprints for creating objects that can store data and do things with it. 
# For example, you can make a class called Animal that has attributes like name, color, and sound, and methods like eat, sleep, and make_noise.

# But to make a class like this, you have to write a lot of code, such as defining a special method called init that sets the attributes when you create an object, 
# and another special method called repr that shows how the object looks like when you print it. 
# Dataclasses help you avoid writing this code by automatically generating these special methods for you. 
# All you have to do is use a decorator called @dataclass and list the attributes and their types. 

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen= True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen= True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmemtation: bool
    params_image_size: list


@dataclass(frozen= True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict 
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int