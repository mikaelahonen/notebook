library(survival)

#Cancer data
data(ovarian)

#Get survival object
s <- Surv(ovarian$futime, 
          ovarian$fustat)

#Fit the model
fit <- survfit(s~1,
               data=ovarian)

#Fit summary
summary(fit)

#Show survival plot with confidence intervals
plot(fit, 
     xlab="time", 
     ylab="probability")
