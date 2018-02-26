#Create data
x <- 1:5
y <- 1:10
df <- data.frame(x,y)

#Fit model
fit <- lm(y~x, data=df)

#Save model to default R working directory
save(fit, file="save-and-load.rdm")

#Remove lm variable
rm(fit)

#Show that it doesn't exist
fit

#Load variable from file
load(file="save-and-load.rdm")

#Show that now it exists again
fit
