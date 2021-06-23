# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}

def updated_damages(damages):
    updated_damages = list()
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        if "M" in damage:
            updated_damages.append(float(damage[0:damage.find("M")]) * conversion["M"])
        if "B" in damage:
            updated_damages.append(float(damage[0:damage.find("B")]) * conversion["B"])
    return updated_damages

updated_damages = updated_damages(damages)
print(updated_damages)


# write your construct hurricane dictionary function here:

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricanes[names[i]] = {"Name": names[i],
                                "Month": months[i],
                                "Year": years[i],
                                "Max Sustained Winds": max_sustained_winds[i],
                                "Areas Affected": areas_affected[i],
                                "Damage": updated_damages[i],
                                "Deaths": deaths[i]}
        
    return hurricanes

hurricane_dictionary = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print(hurricane_dictionary)

# write your construct hurricane by year dictionary function here:

def create_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes_by_year = {}
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricanes_by_year[years[i]] = {"Name": names[i],
                                "Month": months[i],
                                "Year": years[i],
                                "Max Sustained Winds": max_sustained_winds[i],
                                "Areas Affected": areas_affected[i],
                                "Damage": updated_damages[i],
                                "Deaths": deaths[i]}
    return hurricanes_by_year

dictionary_by_year = create_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print(dictionary_by_year)

# write your count affected areas function here:

def create_hurricanes_by_area_dictionary(hurricane_dictionary):
    hurricanes_by_area = {}
    for name in hurricane_dictionary:
        for area in hurricane_dictionary[name]['Areas Affected']:
            if area not in hurricanes_by_area:
                hurricanes_by_area[area] = 1
            else:
                hurricanes_by_area[area] += 1
    return hurricanes_by_area

hurricanes_by_area = create_hurricanes_by_area_dictionary(hurricane_dictionary)
# print(hurricanes_by_area)


# write your find most affected area function here:

def most_hurricanes(hurricanes_by_area):
    values = sorted(list(hurricanes_by_area.values()), reverse=True)
    for area in hurricanes_by_area.keys():
        if values[0] == hurricanes_by_area[area]:
            return area, hurricanes_by_area[area]
       
    
most_hurricanes = most_hurricanes(hurricanes_by_area)

print(most_hurricanes)

# write your greatest number of deaths function here:

def most_deaths(names, deaths):
    most_deaths_dict = {names:deaths for names, deaths in zip(names, deaths)}
    sorted_deaths = sorted(list(most_deaths_dict.values()), reverse = True)
    for names in most_deaths_dict:
        if sorted_deaths[0] == most_deaths_dict[names]:
            return names, most_deaths_dict[names]
    
most_deaths = most_deaths(names, deaths)

print(most_deaths)


# write your catgeorize by mortality function here:

def mortality_scale(hurricane_dictionary):
    hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricane_dictionary:
        num_deaths = hurricane_dictionary[hurricane]["Deaths"]
        if num_deaths == 0:
            hurricanes_by_mortality[0].append(hurricane_dictionary[hurricane])
        elif num_deaths > 0 and num_deaths <= 100:
            hurricanes_by_mortality[1].append(hurricane_dictionary[hurricane])
        elif num_deaths > 100 and num_deaths <= 500:
            hurricanes_by_mortality[2].append(hurricane_dictionary[hurricane])
        elif num_deaths > 500 and num_deaths <= 1000:
            hurricanes_by_mortality[3].append(hurricane_dictionary[hurricane])
        elif num_deaths > 1000 and num_deaths <= 10000:
            hurricanes_by_mortality[4].append(hurricane_dictionary[hurricane])
        else:
            hurricanes_by_mortality[5].append(hurricane_dictionary[hurricane])
    return hurricanes_by_mortality

mortality_scale = mortality_scale(hurricane_dictionary)

print(mortality_scale)


# write your greatest damage function here:

def most_damage(hurricane_dictionary):
    max_damage = 0
    max_damage_hurricane = "Cuba I"
    for hurricane in hurricane_dictionary:
        if hurricane_dictionary[hurricane]["Damage"] == "Damages not recorded": 
            pass
        elif hurricane_dictionary[hurricane]["Damage"] > max_damage:
            max_damage_hurricane = hurricane_dictionary[hurricane]
            max_damage = hurricane_dictionary[hurricane]["Damage"]
    return max_damage_hurricane, max_damage
    
most_damage = most_damage(hurricane_dictionary)

# print(most_damage)

# write your catgeorize by damage function here:
def damage_scale(hurricane_dictionary):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    
    hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for hurricane in hurricane_dictionary:
        damage = hurricane_dictionary[hurricane]["Damage"]
        if damage == "Damages not recorded":
            hurricanes_by_damage[0].append(hurricane_dictionary[hurricane])
        elif damage == damage_scale[0]:
            hurricanes_by_damage[0].append(hurricane_dictionary[hurricane])
        elif damage > damage_scale[0] and damage <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricane_dictionary[hurricane])
        elif damage > damage_scale[1] and damage <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricane_dictionary[hurricane])
        elif damage > damage_scale[2] and damage <= damage_scale[3]:
            hurricanes_by_damage[3].append(hurricane_dictionary[hurricane])
        elif damage > damage_scale[3] and damage <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricane_dictionary[hurricane])
        else:
            hurricanes_by_damage[5].append(hurricane_dictionary[hurricane])
    return hurricanes_by_damage 

damage_scale = damage_scale(hurricane_dictionary)
print(damage_scale)
    