set.seed(1)
group <- sample(c("A","B"), 100, replace=T)
values <- sample(1:10, 100, replace=T)

#Simple summary table
table(values)

#Summary table by group
table(group, values)
