# UFC Fighter Success Factors

---

Author: Mats J Funke

## Motivation and Goal of the project

I've always been intrigued by the factors that influence a fighter's chances of winning a match, whether it's their physical attributes like height and reach, or their fighting style, such as grappling or striking.
Through this data analysis, I aim to uncover insights and answers to these intriguing questions.

## Dataset

I'm conducting my analysis on the [UFC Fighters' Statistics Dataset from Kaggle](!https://www.kaggle.com/datasets/asaniczka/ufc-fighters-statistics).

The overall data quality is generally good, as it's fairly recent and up to date.
However, there were a few rows with missing values that I needed to remove.
I would have appreciated having a gender column in the dataset, but unfortunately, the underlying data is sourced from UFCStats.com, which does not provide gender information.
Fortunately, this shouldn't be a significant issue, as I've categorized the fighters by their weight classes, which will help maintain the analysis's relevance.

# Questions

1. What is the degree of correlation between height and reach, and which is a more significant factor for winning: height or reach?

![height reach plot](./plots/height_reach_plot.png)

The plot above demonstrates that both height and reach are approximately normally distributed, and they exhibit a high correlation coefficient of 0.89, indicating a strong linear dependency between the two variables.

Interestingly, for nearly all weight classes (6 out of 7), having a longer reach is a more reliable predictor of winning than simply being tall.
Especially in the bantamweight, flyweight, middleweight, and light-heavyweight divisions, a longer reach shows a strong correlation with the likelihood of winning.
In contrast, in the welterweight class, simply being taller is more advantageous for winning.

Whats more important strikes or takedowns?

Out of all the columns what is the biggest predictor of fighting Success?
