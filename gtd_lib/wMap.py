import folium, os
import pandas as pd

def wMap(lol):
    # Make a data frame with dots to show on the map    globalterrorismdb_0718dist.csv
    cwd = os.getcwd()
    os.chdir("gtd_lib")

    df = pd.read_csv('gtd_cleaned.csv', sep=',', index_col=0, engine='python', parse_dates=True, encoding=None,
                     tupleize_cols=None, infer_datetime_format=False)

    os.chdir(cwd)
    df = df[~df['city'].isin(['Unknown'])]  # Unknown
    # df = df[~df['city'].isin(['nan'])]               The nan changed into Unknown in dataset
    df = df[~df['longitude'].isin(['nan'])]
    df = df[~df['latitude'].isin(['nan'])]

    # Make an empty map
    m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    # size = df.size
    # times = (size//691)+1
    #print(len(df))

    for i in range(168000, 169000):
        #print(df.iloc[i]['latitude'], df.iloc[i]['longitude'], df.iloc[i]['city'], i)
        folium.Marker([df.iloc[i]['latitude'], df.iloc[i]['longitude']], popup=df.iloc[i]['city']).add_to(m)
    # Save it as html
    m.save('terrorist.html')
    os.system('open terrorist.html')