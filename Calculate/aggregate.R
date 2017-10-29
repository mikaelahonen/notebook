aggregate(d[, 3:4], list(d$Name), mean)

library(plyr)

#Show first 10 rows of data
head(iris,10)

#Count by a single variable
aggregate(iris[, 3:4], list(iris$Species), mean)
          