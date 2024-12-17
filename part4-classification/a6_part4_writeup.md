# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
The model becomes less accurate becoming closer to a 50-50 shot of being correct. This is due to the outliers that could mess up the more accurate mean data.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model is more accurate because it removes outliers from the equation and gives a more accurate representation of the data. The model could be accurate enough for given use case given the right information. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did generally well in predicting when they did and didn't purchase.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
She would not.
