# Election_Analysis



##Project Overview

   A Colorado Board of Election employee  Tom has given a project to us in order to complete the
   election audit of a recent local congressional election for Colarado.The result need to be analyze 
   from  a tabulated results and presented in a form that shows the following details.

###The purpose of this project is:


   1.Calculate the Total number of votes cast.
   2.
   3.Get a complete list of candidates who received votes.
   4.
   5.Calculate the total number of votes each candidate received.
   6.
   7.Calculate the percentage of votes each candidate won.
   8.
   9.Determine the winner of the election based on popular vote.

##Resources

-Data Source:election_results.csv

-Software:Python 3.8.2 ,Visual Studia Code

 Using Python this task becomes automated,so this will help not only to congressional district but can 
 be use in senitorial district and local election.

##Summary

There will be three ways to calculate for voting

 -Mail in Ballot
 
 -Punch card
 
 -Direct Recording Electronic
 
 The fnal result will be the total number of votes received from all this three.
 
 The analysis of the election show that:

-There  were 369,711 votes cast in the election.

![](analysis/Total_votes.png?raw=true)

-The analysis shows that the county are:

  Jefferson
  
  Denver
  
  Arapahoe
  
-The candidate were:

  Charles Casper Stockham
  
  Diana DeGette
  
  Raymon Anthony Doane
  
  
-The county results were :

-The Jefferson county received "10.5%" of the vote and 38,855 number of votes.

-The Denver county received "82.8%" of the vote and 306,055 number of votes.

-The Arapahoe county received "6.7%" of the vote and 24,801 number of votes.

 ![](analysis/County_results.png?raw=true)
 
-The candidate results were:

-The Charles Casper Stockham received "23.0%" of the vote and 85,213 number of votes.

-The Diana DeGette received "73.8%" of the vote and 272,892 number of votes.

-The Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.

 ![](analysis/Candidate_results.png?raw=true)
 
-The winner of the election was:

 Diana DeGette received who received "73.8%" of the vote and 272,892 number of votes.
 
![](analysis/Winner_candidate.png?raw=true)

 ##Challenge Overview
 
 This script can be leveraged in multiple elections, right from local to senatorial and national elections. The script needs to be modified to align with the   governing units like schools, cities, states etc. In certain cases, the data set needs to be enriched with additional information to build hierarchies. Like if the script is used for National elections, separate columns would be needed for Country, State, and maybe even Zones like Midwest USA, or South USA etc.
 The script is build in such a manner that is easy to modify and scale depending on the needs of the election, and hence should be adopted by the election commissioner. 

 ##Challenge Summary

Two changes that can be made to the dataset would be as below:

1. As stated above, geographical hierarchies can be built on this data set to get more insights to the data. If the elections is at a National Level, it would make sense to build a hierarchy (using separate columns) of County -> State -> Zone -> Country
2. Additional information regarding demographies can also be useful. The current data set does not provide valuable information about Voter turnout percentage, income levels, age or ethnicity. We can take it a step further by capturing details like age, ethnicity and income levels at a voter level. This can provide valuable insights of how votes or who does not (it's possible that a 65+ year voter usually does not vote, but most of the people between 25 - 35 years vote as an exmaple). It might also provide crucial information like rich people or males prefer a certain candidate over others, and an example. 
