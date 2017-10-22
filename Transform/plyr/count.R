library(plyr)

#Show first 10 rows of data
head(iris,10)

#Count by a single variable
count(iris, vars="Species")

#Count by two variables
count(iris, vars=c("Species", "Sepal.Length"))

#Leave vars empty to count all combinations
