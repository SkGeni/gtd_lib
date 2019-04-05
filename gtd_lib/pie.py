import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#global eject, top10_country, lab
#data = pd.read_csv('globalterrorismdb_0718dist.csv', sep=',', index_col=0, engine='python',parse_dates=True, encoding=None, tupleize_cols=None, infer_datetime_format=False)
def pie_region(data):
    region = data['region_txt']
    region_agg = dict(region.value_counts())
    regions = region_agg.keys()
    numbers = region_agg.values()
    eject = np.zeros(len(regions))
    eject[0:3] =[0.1,0.1,0.1]
    plt.figure(1)
    plt.title("The regions with the percentage of attacks.")
    plt.pie(numbers,explode=eject,labels=regions,autopct='%1.1f%%')#rotatelabels=20)
    plt.show()

def pie_top10(data):
    country = data['country_txt']
    country_agg = dict(country.value_counts())
    sorted(country_agg)
    country_data = pd.DataFrame.from_dict(country_agg,orient='index')
    top10_country = country_data.iloc[:10]
    eject = np.zeros(len(top10_country))
    lab = top10_country.index.values.tolist()
    eject[0]=0.1
    plt.figure(2)
    plt.pie(top10_country,explode=eject,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Top 10 Countries with the percentage of attacks.")
    plt.show()


def pie_attacktype(data):
    attack_type = data['attacktype1_txt']
    attack_agg = dict(attack_type.value_counts())
    sorted(attack_agg)
    attack_type_data = pd.DataFrame.from_dict(attack_agg,orient='index')
    #top10_country = country_data.iloc[:10]
    eject = np.zeros(len(attack_type_data))
    lab = attack_type_data.index.values.tolist()
    #lab = top10_country.index.values()
    eject[0]=0.1
    plt.figure(3)
    plt.pie(attack_type_data,explode=eject,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Study of several attack types.")
    plt.show()

def sufRatio(data):
    success = data['success']
    success = success.replace([1,0],["Succeeded","Failed"])
    success_agg = dict(success.value_counts())
    success_data = pd.DataFrame.from_dict(success_agg,orient='index')
    eject = np.zeros(len(success_data))
    lab = success_data.index.values.tolist()
    eject[0]=0.1
    plt.figure(4)
    plt.pie(success_data,explode=eject,labels=lab ,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Terrorist Attack : Success Ratio")
    plt.show()


def pie_target(data):
    target_type = data['targtype1_txt']
    target_type_agg = dict(target_type.value_counts())
    sorted(target_type_agg)
    target_type_data = pd.DataFrame.from_dict(target_type_agg,orient='index')
    top10_target_type = target_type_data.iloc[:10]
    eject = np.zeros(len(top10_target_type))
    lab = top10_target_type.index.values.tolist()
    #lab = top10_country.index.values()
    eject[0]=0.1
    plt.figure(5)
    plt.pie(top10_target_type,explode=eject,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Analysis of the Targets of Terrorist Attacks")
    plt.show()

    #######print(data['targetype1_txt']=="Private Citizens & Property")

    #countries = country_agg.keys()
    #num = country_agg.values()
    #plt.subplot(2,1,2)

    #relevant_data = data['iyear','imonth', 'iday',  ]

def pie_claim(data):
    claimed = data['claimed']
    claimed = claimed.replace([1,0,None],["Claimed","Non-Claimed","Unknown"])
    claimed_agg = dict(claimed.value_counts())
    claimed_data = pd.DataFrame.from_dict(claimed_agg,orient='index')
    eject = np.zeros(len(claimed_data))
    lab = claimed_data.index.values.tolist()
    eject[0]=0.1
    plt.figure(6)
    plt.pie(claimed_data,explode=eject,labels=lab ,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Do they claim for the attack.")
    plt.show()

    claimmode_txt = data['claimmode_txt']
    claimmode_txt_agg = dict(claimmode_txt.value_counts())
    claimmode_txt_data = pd.DataFrame.from_dict(claimmode_txt_agg,orient='index')
    eject = np.zeros(len(claimmode_txt_data))
    lab = claimmode_txt_data.index.values.tolist()
    eject[0]=0.1
    plt.figure(7)
    plt.pie(claimmode_txt_data,explode=eject,labels=lab ,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Claiming Methods for terrorists")
    plt.show()

def pie_weapon(data):
    weaptype1_txt = data['weaptype1_txt']
    weaptype1_txt_agg = dict(weaptype1_txt.value_counts())
    weaptype1_txt_data = pd.DataFrame.from_dict(weaptype1_txt_agg,orient='index')
    lab = weaptype1_txt_data.index.values.tolist()
    plt.figure(8)
    plt.pie(weaptype1_txt_data,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Weapon study of terrorist attacks")
    plt.show()

'''
def pie_property(data):
    property = data['property']
    property = property.replace([1,0],['Property Damaging Attacks', 'No Property Damage'])
    property_agg = dict(property.value_counts())
    property_data = pd.DataFrame.from_dict(property_agg,orient='index')
    lab = property_data.index.values.tolist()
    plt.figure(8)
    plt.pie(property_data,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
    plt.title("Property Damage Analysis of Terrorist Attacks")
    plt.show()

'''