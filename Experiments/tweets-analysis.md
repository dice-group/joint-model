# Our Tweets Analysis of Typhoons between 2006-2016
Typhoon environmental data are tracked periodically (i.e. at regular time intervals) before, during and after they strike.
The goal of our work is to detect the intensity of typhoons not only based on such environmental data but also based on data collected by humans in the form of social media posts during each of the typhoons under study.
To pair social media with the environmental data of typhoons, we collect all tweets posted within the time slot of the respective environmental data into one batch. 

Inspired by the work of [1,2], we thus analyzed the volume of tweets as well as sentiments during different time slots of typhoons. We visualized our tweets analysis in <img src="https://github.com/dice-group/joint-model/blob/master/Experiments/tweets_analysis.png" alt="Kitten"
	title="Tweets Analysis" width="150" height="100" />, the upper row of plots depicts our content analysis of tweets during four different typhoons,
where we explored how typhoon intensities vary during typhoon days.
In the middle row of plot of the same figure, we present the count of tweets within the same time slots of the provided intensity in the upper row.

Finally, the lower 4 plots present count of tweets with  positive (in blue) and negative (in yellow) sentiment. 
Comparing the respective plots of intensity, tweets count and sentiments for each of the 4 typhoons, we are able to see the correlation between typhoon's intensity and tweets count and sentiment. To this end, we use the count of tweets and their sentiments as additional indicators for predicting typhoon intensity. 

+ [1] Kryvasheyeu Y, Chen H, Obradovich N, Moro E, Van Hentenryck P, Fowler J, Cebrian M. Rapid assessment of disaster damage using social media activity. Science advances. 2016 Mar 1;2(3):e1500779.
+ [2] He J, Shen W, Divakaruni P, Wynter L, Lawrence R. Improving traffic prediction with tweet semantics. InTwenty-Third International Joint Conference on Artificial Intelligence 2013 Jun 30.
