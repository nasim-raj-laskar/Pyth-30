# Weather Temperature Prediction Using LSTM

## Description
This [project](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Weather%20Prediction/weather-prediction-lstm.ipynb) focuses on predicting daily average temperatures using a Long Short-Term Memory (LSTM) neural network. By utilizing historical weather data, the project preprocesses, normalizes, and trains an LSTM model to forecast future temperature values. The model is validated and evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). Visualizations of predictions, confidence intervals, and residuals provide insights into the model's performance.

## Tools Used
- **Python**: Core programming language for data analysis and deep learning.
- **Libraries**:
  - `pandas`: Data manipulation and resampling.
  - `numpy`: Numerical operations.
  - `matplotlib` & `seaborn`: Data visualization.
  - `scikit-learn`: Data normalization and evaluation metrics.
  - `TensorFlow/Keras`: Building and training the LSTM model.
- **Callbacks**:
  - `EarlyStopping`: Prevents overfitting by stopping training early.
  - `ModelCheckpoint`: Saves the best-performing model during training.

## Output Visualization
1. **Temperature Prediction vs Actual**: Comparison of predicted temperatures with actual values over time.
   <img src="https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Weather%20Prediction/img/1.png" alt="Prediction vs Actual" width="600"/>

2. **Confidence Interval Plot**: Visualizing uncertainty in predictions with a 95% confidence interval.
   <img src="https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Weather%20Prediction/img/2.png" alt="Confidence Interval" width="600"/>

3. **Residual Plot**: Scatter plot of residuals to evaluate prediction errors.
   <img src="https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Weather%20Prediction/img/3.png" alt="Residual Plot" width="600"/>


