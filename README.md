# Beagles_vs_Bagles
All in all this is learngin/ fun project mostly for me (Also a first draft) <br>

## Project definition

This project aims to use images from sites like GettyImages and so on to feed into a Machine Learning classifier to find out, whether or not the images contains a beagle or a bagle (cheesy word play I know :D).
It tries to help get confident in TDD and other methods as well as deepen my knowledge in Data Engineering and Machine Learning and is therefore not to taken seriously. You will find different comments here and there about code coverage etc. that aren't meant for others but mostly for me. 

## Project Build

### Data Pipeline
The data Pipeline consists of a webcrawler and a download. They are both using the API provided by GettyImages etc. to find all suitable images, under a given set of keywords and are then downloaded, given they don't already exist within the data set. To remove these duplicates a data warehouse will therefore be needed (see following point). After finding all the images suitable for download, the metadata database will then be searched for duplicates of the images using authors and name of the images. 

### Data Warehouse

### Machine Learning/ Deep Learning algorithm
