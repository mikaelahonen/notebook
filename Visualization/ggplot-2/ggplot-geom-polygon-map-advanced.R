library("ggplot2")

#Labels
labels <- data.frame(
  long = c(-43.1729, 151.2093),
  lat = c(-22.9068, -33.8688),
  names = c("Rio de Janeiro", "Sydney"),
  stringsAsFactors = FALSE
)  

#World map
world <- map_data("world") #world2 to center on International date line
world$long <- world$long
color <- ifelse(world$region=="Finland", "green", "gray")
ggplot() + 
  geom_polygon(data = world, aes(x=long, y = lat, group = group), fill=color, colour="white") +
  coord_fixed(1.3) +
  geom_point(data = labels, aes(x = long, y = lat), color = "black", size = 5) +
  geom_point(data = labels, aes(x = long, y = lat), color = "yellow", size = 4) +
  geom_text(data = labels, aes(label = names, x = long, y = lat)) +
  #coord_equal(xlim = c(-90,-30), ylim = c(-60, 20)) + #Zoom to a location
  labs(x = "Longitude", y = "Latitude", title = "World Map")
  