library(class)

#Randomize the order of data
order <- sample(nrow(iris))
d.sample <- iris[order,]

#Show first rows
head(d.sample)

#Train and test data
train.data <- d.sample[1:100, 1:4]
train.labels <- d.sample[1:100, 5]
test.data <- d.sample[101:150, 1:4]
test.labels <- d.sample[101:150, 5]

#Get labels from knn
knn.labels <- knn(train.data, test.data, train.labels)

#Get success ratio
ratio <- mean(test.labels == knn.labels)
ratio
