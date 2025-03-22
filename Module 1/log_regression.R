library(tidyverse)

# Load the first dataset
shoe <- read.csv('shoe-size-samples.csv')
view(shoe)

# Load the prediction dataset
shoe_val <- read.csv('class_shoe_sizes_v2_2024_1.csv')

outlierless <- shoe %>% 
  # remove the outliers because they're obvious errors
  filter(height > 10 & shoe_size < 80) %>% 
  # make the binary column
  mutate(sex_binary = ifelse(sex == 'woman', 0, 1))

# plot(shoe_size ~ height, data = shoe, col = as.factor(sex))
# plot(shoe_size ~ height, data = outlierless, col = as.factor(sex))

# Logistic regression that predicts sex based on shoe size
shoe_lm <- glm(sex_binary ~ shoe_size, data = outlierless, family = 'binomial')
b <- coef(shoe_lm)

# Plot of that prediction
plot(sex_binary ~ shoe_size, data = outlierless)
curve(exp(b[1] + b[2]*x) / (1 + exp(b[1] + b[2]*x)), add = TRUE)

# Interpretations - summary, and 
summary(shoe_lm)
exp(b[2])



