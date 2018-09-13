#https://magesblog.com/post/2013-03-12-how-to-use-optim-in-r/

#Optimize linear function y = a * x + b by minimizing sum of squared residuals
#optim function does the optimization by varying the parameters

#Initialize data
d <- data.frame(x=c(1,2,3,4,5,6), 
               y=c(1,3,5,6,8,12))

#Plot data
plot(d)


#declare the function
min.rss = function(data.arg, par){
  with(data.arg, sum((par[1]*x+par[2]-y)^2))
}

#Run the optimization
#set initial values for par argument
result <- optim(par=c(0, 1), fn=min.rss, data=d)

#Show results
print(result)