'''Standard Python Package Imports'''
import lightning.pytorch as pl
from lightning.pytorch.callbacks import EarlyStopping, LearningRateFinder
from lightning.pytorch.tuner import Tuner
from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer

data = ...

# defining the dataset
max_encoder_length = 0
max_prediction_length = 0
training_cutoff = 'YYYY-MM-DD'

training = TimeSeriesDataSet(
    data[lambda x: x.date < training_cutoff],
    time_idx = ...,
    target = ...,
    weight = "weight",
    group_ids= [...],
    max_encoder_length = max_encoder_length,
    max_prediction_length= max_prediction_length,
    static_categoricals= [...],
    static_reals= [...],
    time_varying_known_categoricals=[ ... ],
    time_varying_known_reals=[ ... ],
    time_varying_unknown_categoricals=[ ... ],
    time_varying_unknown_reals=[ ... ],
)

validation = TimeSeriesDataSet.from_dataset(training,data, min_prediction_idx=training.index.time.max() + 1, stop_randomization=True)
batch_size = 64
train_dataloader = training.to_dataloader(train=True, batch_size=batch_size, num_workers=2)
val_dataloader = validation.to_dataloader(train=False,batch_size=batch_size, num_workers=2)