library(ggplot2)

#Time series sequence number
time <- 0:20

#Arbitrary value for time series
set.seed(1)
value <- sample(1:10,21,replace=T)+time

#Set decay constant
decay <- 0.5
#Create exponential downweighting vector
dw <- decay^(20-time)
#Value multiplied by exponential downweighting factor 
value.dw <- dw*value

value.estimate <- cumsum(value.dw)/cumsum(dw)

#Extra: Calculate the half life with give decay
-log(2)/log(decay)

#Take data to data frame for plot
data.plot <- data.frame(time,value,value.estimate)

#Draw plot from actual and downweighted data
ggplot(data=data.plot, aes(x=time))+
  geom_line(aes(y=value))+
  geom_line(aes(y=value.estimate), color="blue")
