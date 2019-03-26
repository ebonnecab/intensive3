#pkgs for data wrangling
library(tidyr)
library(stringr)
library(magrittr)
library(dplyr)
library(lubridate)

#for sentiment analysis
library(tidytext)

#for visualization
library(ggplot2)
library(ggridges)

#import word_tokens
Word_tokens <- read.csv("/Users/admin/dev/Ebonne_Coding_Project/intensive3-3/v2.csv", header=TRUE, stringsAsFactors=FALSE) 