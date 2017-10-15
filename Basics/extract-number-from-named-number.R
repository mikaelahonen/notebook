#Create named numbers
values = c(100, 200)
names(values) = c("Value 1", "Value 2")

#Option 1: By index
values[[1]]

#Option 2: By name
values[["Value 1"]]