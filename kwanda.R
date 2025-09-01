install.packages("readxl")
library(readxl)
install.packages('tidyverse')
library(tidyverse)


file_path <- "https://raw.githubusercontent.com/kwanda2426/projects/main/sebokeng_data.xlsx"
temp_file <- tempfile(fileext = ".xlsx")
download.file(file_path, destfile = temp_file, mode = "wb")

# Read the Excel file
data <- read_excel(temp_file)
View(data)

mean_ <- mean(data$sebSO2, na.rm = TRUE)
print(mean_)

ggplot(data,aes (x = sebSO2)) + 
  geom_histogram() + labs(x = "Kwanda")

