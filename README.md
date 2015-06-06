# Cryme

Cryme is a web application built with Flask that uses machine learning to analyze crime history in Washington D.C. and makes predictions. Cryme was built at BitCamp, a hackathon hosted at the University of Maryland. You can view the ChallengePost project [here](http://challengepost.com/software/cryme-3gv4).

## Screenshots

### Cryme Front Page

![Cryme Front Page](https://s3.amazonaws.com/fvd-data/notes/166489/1433616517-ADwvG2/screen.png)

### Choosing a time and location

![Filling out the form](https://s3.amazonaws.com/fvd-data/notes/166489/1433615028-e78rWH/screen.png)

## Inspiration

Our team has plenty of machine learning experience, so we wanted to work with and train with a large amount of data to make predictions. The Washington D.C. Open Data Catalog is full of data sets of all kinds, so we narrowed it down to data that would be of use to D.C. residents. Crime history is really big, so many places in D.C. are dangerous. Cryme allows the end user to determine the potential danger for any location in D.C. at any time.

## How it works

Simply proceed to the dashboard where you'll be presented with a form and a map. The map is pulled from the Google Maps API and you can choose to either submit data directly via the form or to click on the map to extract the information. Select the time of day you may happen to walk in your location of choice. Submit the information you've entered to see the prediction. There is search history available for you to view your past searches.

## Challenges

A lot of the data for Cryme is restricted - there aren't many criteria to go by besides the type of crime and location it occurred in. Having more data would help us improve the predictions in the long run. Google Maps API also has its limits in gathering map data, so we have to take that into account when proceeding with the project in the future.

## Future Plans

Machine learning is really fun, but a lack of data isn't as much. More data could mean higher accuracy and a broader set of results. We hope to look at other sources of crime data for D.C. to retrain the system and improve results.

## Project Authors

- Taylor Foxhall ([@hallfox](https://github.com/hallfox))
- Gabriel Ochoa ([@gabeochoa](https://github.com/gabeochoa))
- Alan Plotko ([@alanplotko](https://github.com/alanplotko))
