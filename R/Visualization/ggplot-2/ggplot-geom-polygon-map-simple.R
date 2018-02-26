library("ggplot2")

#Finland
fin <- map_data("world2", "finland")
ggplot(data = fin, aes(x=long, y = lat, group = group)) + geom_polygon()