import pandas as pd
import numpy as np

world_pop = pd.read_csv("C:/Users/spenc/OneDrive/Documents/School/Fall 2022/CSE 310 - Applied Programming/data framework/world_population.csv")

def top_5_pop(world_pop):
    world_pop = world_pop.sort_values(by=['Rank'], axis = 0)
    print(world_pop[world_pop['Rank'] < 6])

def total_pop(world_pop):
    total_pop = world_pop.filter(like = 'Population')
    total_pop = total_pop.drop('World Population Percentage', axis = 1)
    total_pop = total_pop.agg(sum)

    print("\nTotal Population Over Time:")
    print(total_pop)


top_5_pop(world_pop)
total_pop(world_pop)