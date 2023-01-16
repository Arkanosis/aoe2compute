#! /usr/bin/env python3

# Bohemians 23+2 FC on Arena

## Constants

starting_villagers = 3
house_wood = 25
lumber_camp_wood = 100
mill_wood = 100
villager_food = 50
feudal_food = 500
farm_wood = 60
blacksmith_wood = 50 # bohemians only
market_wood = 175
castle_food = 800
castle_gold = 200
berry_bush_food = 125
sheep_food = 100
deer_food = 140
boar_food = 340
farm_food = 175
double_bit_axe_wood = 50
double_bit_axe_food = 100
horse_collar_wood = 75
horse_collar_food = 75
bow_saw_wood = 150
bow_saw_food = 100
heavy_plow_wood = 125
heavy_plow_food = 125

## Initialization

wood_needed = -200
food_needed = -200
gold_needed = -100
stone_needed = -200

## Dark age

wood_needed += 4 * house_wood
wood_needed += 1 * lumber_camp_wood
wood_needed += 1 * mill_wood

food_needed += (23 - starting_villagers) * villager_food
food_needed += feudal_food

print(f'Needed for feudal: {wood_needed} wood, {food_needed} food')

## Feudal age

food_needed += 2 * villager_food

wood_needed += 2 * farm_wood
wood_needed += 1 * house_wood
wood_needed += 1 * blacksmith_wood
wood_needed += 1 * market_wood

food_needed += castle_food
gold_needed += castle_gold

print(f'Needed for castle: {wood_needed} wood, {food_needed} food, {gold_needed} gold')

food_available = 0

food_available += 8 * sheep_food
food_available += 6 * berry_bush_food
food_available += 3 * deer_food # sometimes 4
food_available += 2 * boar_food # sometimes 4

print(f'Available: {food_available} food')

# Castle age

wood_needed += double_bit_axe_wood
food_needed += double_bit_axe_food

wood_needed += horse_collar_wood
food_needed += horse_collar_food

print(f'Needed for castle with feudal eco: {wood_needed} wood, {food_needed} food, {gold_needed} gold')

wood_needed += bow_saw_wood
food_needed += bow_saw_food

wood_needed += heavy_plow_wood
food_needed += heavy_plow_food

print(f'Needed for castle with castle eco: {wood_needed} wood, {food_needed} food, {gold_needed} gold')
