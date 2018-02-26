# Country and Gender vector length 24
category <- c(rep("China - M",6),rep("USA - M",6),rep("China - F",6),rep("USA - F",6))

# Wight vector length 24
weight <- c(rep(70, 6),rep(100, 6),rep(50, 6),rep(80, 6))
weight <- weight + rnorm(24)*10

#To data.frame
df <- data.frame(category, weight)
View(df)

#These will have the same result
pairwise.t.test(weight, category)