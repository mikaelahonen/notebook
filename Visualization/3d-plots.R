#rgl library plot3d function
#appears in new window
library(rgl)
attach(iris)
plot3d(Sepal.Length, Sepal.Width, Petal.Length, type="s", col=as.numeric(Species), size=1)

#plot_ly from plotly library
#opens in viewer tab in RStudio
library("plotly")
plot_ly(data=iris, x=Sepal.Length, y=Sepal.Width, z=Petal.Length, type="scatter3d", mode="markers")