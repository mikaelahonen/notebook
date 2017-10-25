x.1 <- runif(5,1,3)
x.2 <- runif(5,2,4)
x <- c(x.1, x.2)

y.1 <- runif(5,1,3)
y.2 <- runif(5,2,4)
y <- c(y.1, y.2)
  
observations <- data.frame(x,y) 

#nstart: how many different start centroids
clusters <- kmeans(observations, 2, iter.max=10, nstart=5)

#Predicted clusters
clusters$cluster

#Cluster centers
clusters$centers

#cluster sizes
clusters$size

#iteration that gave the results
clusters$iter

#whithinss: sum of squares compared to centroids
clusters$withinss

#betweenss: sum of squares for centroids compared to gloabl mean

#totss: total sum of squares when compared to global mean = withinss + betweenss
clusters$totss

#This ratio is good measure for total accuracy
clusters$betweenss / clusters$totss
