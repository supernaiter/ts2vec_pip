# TS2Vec

This is a pip-installable fork of [TS2Vec](https://github.com/zhihanyue/ts2vec), which is a time series representation learning framework introduced in the paper [TS2Vec: Towards Universal Representation of Time Series](https://arxiv.org/abs/2106.10466) (AAAI-22).

The main purpose of this fork is to make the original implementation easily installable via pip, while maintaining all the functionality of the original work.

## Installation

```bash
pip install git+https://github.com/supernaiter/ts2vec_pip.git
```

## Requirements

* Python >= 3.7
* torch
* scipy
* numpy
* pandas
* scikit_learn
* statsmodels
* Bottleneck

## Usage Example

```python
from ts2vec import TS2Vec
import numpy as np

# Generate sample data
train_data = np.random.rand(100, 200, 1)  # 100 instances, 200 timestamps, 1 feature

# Train a TS2Vec model
model = TS2Vec(
    input_dims=1,
    device=0,
    output_dims=320
)
loss_log = model.fit(
    train_data,
    verbose=True
)

# Compute timestamp-level representations
repr = model.encode(train_data)  # shape: n_instances x n_timestamps x output_dims

# Compute instance-level representations
repr = model.encode(train_data, encoding_window='full_series')  # shape: n_instances x output_dims

# Sliding inference
repr = model.encode(
    train_data,
    causal=True,
    sliding_length=1,
    sliding_padding=50
)  # shape: n_instances x n_timestamps x output_dims
```

For more detailed documentation and examples, please refer to the [original repository](https://github.com/zhihanyue/ts2vec).
