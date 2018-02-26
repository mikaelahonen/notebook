# Calculate
Functions and scripts that do simple calculations
for data.

## `apply()`, `lapply()`, `sapply()`, `tapply()`
`apply()` executes a function for each row or column.
Use `1` as the seconds parameter for rowwise calculation
and `2` for columnwise calculation.

`lapply()` works pretty much same way but takes 
a list as an input and also return a list.

`sapply()` is like `lapply()` but it returns a vector
or matrix.

Apply a function for each group separately with `tapply()`.

## Name of maximum column per row
For each row return the name of the column 
that has the maximum value.

## Table
Create summery tables from variables.
Table is a matrix data type.

## `which.max()` and `which.min()`
Return index of maximum or minimum values.
