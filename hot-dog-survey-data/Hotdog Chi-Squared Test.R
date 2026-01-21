library(stats)

setwd("C:/Users/dinos/OneDrive/Desktop/College/8th Semester")
getwd()

data <- read.csv("Cleaned Hotdog Data.csv")
data

contingency_table <- table(data$Year, data$Hotdog.a.Sandwich.)
contingency_table

chisq.test(contingency_table, simulate.p.value = TRUE, B = 100000)
