# Time Series
Time series are different from traditional statistical models
in a way that the sequence of the observations is significant.
This means that previous observations might be helpful
in predictions.

## ARIMA
AutoRegressive Integrated Moving Average.

## Auto correlation
Cross correlation with the series itself.

## Autoregressive-model
It can be used to predict future values.

## Cross correlation
Investigate time series correlations with different lags.

## Survival analysis
Answers to the question: What time it takes for an event to occur?
The value is always greater than zero.
Incompletely observed responses are censored.

Right censoring means that a subject doesn't experience the event before the study ends.
There are three main reasons for censoring:
* The event doesn't occur before the end of the study
* A subject can not be reached for whatever reason
* A subject withdraws from the study

When the event has occured before the study begins it is called left censoring.

[Read more](http://www.stat.columbia.edu/~madigan/W2025/notes/survival.pdf).

Examples:
* Time until tumor recurrence
* Time to machine failure

In other fields:
* Social sciences: Event history analysis
* Engineering: Reliability analysis