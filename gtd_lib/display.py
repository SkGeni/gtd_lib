import difflib

#display by year range
#eg: ,1990, 2017
def display(data,min_year, max_year):
    if(min_year<max(data['iyear']) & max_year >min(data['iyear'])):             #if year is out of range return -1
        return -1

    req = data.loc[(data['iyear'] >= min_year) & (data['iyear'] <= max_year)]
    return req


#display year by recency
#eg: 7 years
def display_recency(data,years):
    if (max(data['iyear'])-min(data['iyear'])-1<years):                         #if number of years is more than in database
        return -1
    req = data.loc[(data['iyear'] >=(max(data['iyear'])-years) ) &
                   (data['iyear'] <= max(data['iyear']))&
                   (max(data['iyear'])-years!=1993)]                            #as 1993 data is not available
    return req


def display_country(data, country):
    req = data.loc[data['country_txt'].str.lower() == country.lower()]
    return req


def display_city(data, city):
    req = data.loc[data['city_txt'].str.lower() == city.lower()]
    return req

#display by attack_type
#encoded in 9 different attack types:
#   1: Assassination
#     2: Armed Assault
#     3: Bombing/Explosion
#     4: Hijacking
#     5: Hostage Taking (Barricade Incident)
#     6: Hostage Taking (Kidnapping)
#     7: Facility/Infrastructure Attack
#     8: Unarmed Assault
#     9: Unknown
def display_attack(data,attack):
    req = data.loc[data['attacktype1'] == attack]
    return req

#display based on success andd failure
def display_success(data,flag):
    req = data.loc[data['success'] == flag]
    return req

#based on target in strings
def display_target(data, target):
    for x in data['target1'].dropna():
        sequence = difflib.SequenceMatcher(isjunk=None,a=x,b=target)
        difference = sequence.ratio()*100
        difference =round(difference,1)

    req = data.loc[data['target1'].str.lower() == target.lower()]
    return req

#base on target type
def display_tar_type(data, tar_typ):
    for x in data['targtype1_txt'].dropna():
        sequence = difflib.SequenceMatcher(isjunk=None,a=x,b=tar_typ)
        difference = sequence.ratio()*100
        difference =round(difference,1)

    req = data.loc[data['targtype1_txt'].str.lower() == tar_typ.lower()]
    return req


#based on target subtype
def display_tar_subtype(data, tar_subtyp):
    for x in data['targsubtype1_txt'].dropna():
        sequence = difflib.SequenceMatcher(isjunk=None,a=x,b=tar_subtyp)
        difference = sequence.ratio()*100
        difference =round(difference,1)

    req = data.loc[data['targsubtype1_txt'].str.lower() == tar_subtyp.lower()]
    return req

#based on the terrorist group name
def display_terrorist(data, terr):
    req = data.loc[data['gname'].str.lower() == terr.lower()]
    return req

# based on weaptype1_txt
def display_terrorist(data, weap):
    req = data.loc[data['weaptype1_txt'].str.lower() == weap.lower()]
    return req


