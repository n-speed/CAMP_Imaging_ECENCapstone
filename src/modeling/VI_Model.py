'''Standard Python Package Imports'''
import lightning.pytorch as pl
from lightning.pytorch.callbacks import EarlyStopping, LearningRateFinder
from lightning.pytorch.loggers import TensorBoardLogger

from pytorch_forecasting import Baseline, TemporalFusionTransformer, TimeSeriesDataSet
from pytorch_forecasting.data import GroupNormalizer
from pytorch_forecasting.metrics import MAE, SMAPE, PoissonLoss, QuantileLoss
from pytorch_forecasting.models.temporal_fusion_transformer.tuning import optimize_hyperparameters

from pytorch_forecasting.data.examples import get_stallion_data

# defining the dataset
data["time_idx"] = data["data"].dt.year * 12 + data["data"].dt.month
data["time_idx"] -= data["time_idx"].min()



