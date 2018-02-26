# Time Series
Time series are different from traditional statistical models
in a way that the sequence of the observations is significant.
This means that previous observations might be helpful
in predictions.

On the other hand you have to be careful from what period you use data.
For example training data must be taken from period before test data.

## ARIMA
AutoRegressive Integrated Moving Average.

## Auto correlation
Cross correlation with the series itself.

## Autoregressive-model
It can be used to predict future values.

## Cross correlation
Investigate time series correlations with different lags.

## Decompose trend and seasonality

Extract trend, seasonality and random values from time series.
Select either additive or multiplicative model.

[Additive and multiplicative decomposition](https://anomaly.io/seasonal-trend-decomposition-in-r/).

<b>Additive</b>
`Time series = Seasonal + Trend + Random`
Seasonal variation is somewhat constant.

<b>Multiplicative</b>
`Time series = Seasonal * Trend * Random`
Seasonality increases with the trend.

Additive process considering monthly data:
* <b>Trend</b>: Get running mean from past 12 months.
* <b>Seasonality</b>: Substract trend from original values and calculate mean for each month.
* <b>Random</b>: Substract trend and and seasonality from original values.
* For multiplicative series divide instead of substracting.

<b>stl()</b>
Only for additive time series.

## Exponential downweighting
Calculate a coefficient that fades when you go further to past.
It's more realistic than simply taking moving average
where all past observations are equally important.
Also wtih exponential downweighting there's no need to
specify how many past observations to use.
The fading constant is called the `decay`.

Doesn't work for data with trends. 
For growing data the downweighted estimate would be always behind. 

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

## Trend and seasonality decomposition



Process
1. <b>Detect the seasonality</b> length by moving average for example.
2. <b>Detrend</b>. 