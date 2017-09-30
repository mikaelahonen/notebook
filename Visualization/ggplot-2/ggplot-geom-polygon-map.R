library("ggplot2")
fin <- map_data("world2", "finland")
ggplot() + geom_polygon(data = fin, aes(x=long, y = lat, group = group))