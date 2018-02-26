# `ggplot 2` library #

Some simple R plots made with `ggplot2` graphics library to get started quickly.
* Great [cheatsheet](https://www.rstudio.com/resources/cheatsheets/) for ggplot2 in RStudio web page.
* Use `qplot()` for less detailed plots
* Use `ggplot()` together with additional definitions for more detailed plots
* Define dataset and variable mappings in `ggplot()` base function
* Use geom_ functions with `ggplot()` to actually draw plots. For example `ggplot() + geom_point()`

## ggplot-geom-polygon-map-advanced ##
* (Examples)[http://eriqande.github.io/rep-res-web/lectures/making-maps-with-R.html]

# mapping=aes()
For `mapping` parameter use `aes()` function to set axes.
You can set it in main `ggplot()` function or in other functions
such as `geom_point()`.

You can also set common x variable in maint function and 
y variables individually for each sub plot.
