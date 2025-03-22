library(tidyverse)

shoe_val <- read.csv('women.csv')
view(shoe_val)

shoe_lm <- lm(shoe_size ~ height, data = shoe_val)
summary(shoe_lm)

plot(shoe_size ~ height, data = shoe_val)
abline(shoe_lm)
#y = 19.46653 + 0.11181 * x