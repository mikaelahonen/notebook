library(zoo)

#Simple oredered data
x <- 1:10

#fill = NA
#align: where to pick the index of the result
rollmean(x, 3, fill=NA, align="right")
rollsum(x, 3, fill=NA)
rollmax(x, 3)
rollmedian(x, 3)

#Generic roll method with custom function
#rollapplyr is the same but defaults to align=right
rollapply(x, 3, FUN=function(x) if(sum(x)>10){"Big"}else{"Small"})
