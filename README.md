# Beagles_vs_Bagles
All in all this is learngin/ fun project mostly for me (Also a first draft) <br>

## Project definition

This project aims to use images from sites like GettyImages and so on to feed into a Machine Learning classifier to find out, whether or not the images contains a beagle or a bagle (cheesy word play I know :D).
It tries to help get confident in TDD and other methods as well as deepen my knowledge in Data Engineering and Machine Learning and is therefore not to taken seriously. You will find different comments here and there about code coverage etc. that aren't meant for others but mostly for me. 

## Project Build

### Data Pipeline
The data Pipeline consists of a webcrawler and a download. They are both using the API provided by GettyImages etc. to find all suitable images, under a given set of keywords. Metadata will then be collected, cleansed and normalized and then checked against the metadata database to find duplicates, that already exist within the image database. These images will then be discarded for download and only those, that do not exist, will be downloaded and fed into the database alongside its metadata. 

### Data Warehouse

### Machine Learning/ Deep Learning algorithm
