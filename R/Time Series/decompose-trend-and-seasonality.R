#Fake data during 3 years monthly 
set.seed(1)
id <- 1:36
year <- c(rep(2015,12),rep(2016,12),rep(2017,12))
month <- rep(1:12,3)
#Trend
trend <- 1:36

#Seasonality for additive model
seasonality.year <- c(2,4,3,5,6,7,8,5,5,4,3,2)
seasonality <- rep(seasonality.year, 3) 

#Randomness for additive model
random <- runif(36,-2,2)

#Create additive time series
ts <- ts(trend + seasonality + random, frequency=12)

#Run decompose() and stl() functions
ts.dc <- decompose(ts, type="additive")
ts.stl <- stl(ts, s.window = 12)

#Draw plots
plot(ts.dc)
plot(ts.stl, main="stl()")
