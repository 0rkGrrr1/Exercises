import geopandas as gpd

def plot_post_code_map():
    """ Function processes raw data,
    extracts data from column POSTNUMMER,
    draws the map of given post codes,
    and prints all unique post codes to console. """
    
    #Reading data set:
    norway_set = gpd.read_file('Basisdata_0000_Norge_25833_Postnummeromrader_SOSI_Postnummerområde_FLATE.shp')
    
    #Choosing essential columns:
    norway_set = norway_set[['POSTNUMMER', 'geometry']]
    
    #Drawing a map with outline of every postal code:
    norway_set.plot(figsize=(10, 10), column='POSTNUMMER', cmap='prism',
                    edgecolor='black', linewidth=0.2)
   

    #Selecting unique postal codes                     
    for item in norway_set[['POSTNUMMER']][:-1]:
        uniquelist = norway_set[item].unique()
    
    #Displaying total count of unique postal codes   
    print('Number of unique rows:')
    print(uniquelist.size)
        
    #Printing all unique post codes
    print('Unique post codes:') 
    print(uniquelist.tolist())

    
plot_post_code_map()



