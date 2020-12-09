# mrsmith

This is a simple library to generate random names based of the 1990 US Census data. Names are choosen with the same random distrubution found in the census.     
Additionally the race category can be specified to use a specific distribution. 

# Using mrsmith
To generate a random name simply import the package and call one of these methods with race and gender being optional parameters.

    mrsmith.full_name() # Returns a random first and last name of any race/gender as a tuple
    mrsmith.full_name("hispanic", "male") # Returns a random first and last name of the specified race and gender
    mrsmith.first_name("aian", "female") # Returns a random first name
    mrsmith.last_name("api") # Returns a random last name
    
# How It Works
The data used for this library is a list of names that includes the proportion of people with that name and a percentage for how many people with that name fall into each race category.    

A separate data from the Social Security Administration set was used to split the first names into Male and Female. This split assumed all races had the same Male/Female ratio for each name.     

This library will choose a random first and last name from these data sets with the same distribution. So if there were twice as many boys named John compated to Mark then John will be twice as likely when generating a name. 

# Race Categories
These are the categories used in the census data.

White   
Black    
API - Asian, Pascific Island    
AIAN - American Indian, Alaskan Native    
Hispanic    
