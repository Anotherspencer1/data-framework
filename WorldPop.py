import pandas as pd
import numpy as np

#Use pandas to read our csv file to dataframe world_pop
world_pop = pd.read_csv("world_population.csv")

#This function takes a given country and displays the information for that country.
def country_pop(world_pop, country):
    
    if country not in world_pop['Country/Territory'].values: #Checks to see if country exists. If not prints error, if it does prints output
        print("\nERROR: Country not found\n")
    else:
        print(f"\n==================== Information on {country} =====================")
        print(world_pop[world_pop['Country/Territory'] == country])
        print("====================================================================")

#This sorts the dataframe according to the rank column and then displays the top 5 countries by rank.
def top_5_pop(world_pop):
    world_pop = world_pop.sort_values(by=['Rank'], axis = 0)
    print("\n=================== Top 5 Countries By Population ==================")
    print(world_pop[world_pop['Rank'] < 6])
    print("====================================================================")

#This filters the dataframe and just returns the total world population over time
def total_pop(world_pop):
    total_pop = world_pop.filter(like = 'Population') #Isolates the columns containing 'Population
    total_pop = total_pop.drop('World Population Percentage', axis = 1) #We remove this irrelevant column
    total_pop = total_pop.agg(sum) #Adds up values from every row into one grand total for each column

    print("\n=================== Total Population Over Time =====================")
    print(total_pop)
    print("====================================================================")




country = input("What country would you like information about? ").capitalize() #Takes user input for a country and capitalizes it
country_pop(world_pop, country)
top_5_pop(world_pop)
total_pop(world_pop)