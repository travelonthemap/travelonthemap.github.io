"""
generate the markdown page for all countries
"""
from os import path
all_countries_filename = 'all_countries.csv'
countries_path = '../_places/'

all_countries = open(all_countries_filename, 'r')
for country in all_countries:
    name, code = country.split(',')
    country_filename = name.replace(' ','_').replace("'",'').replace('(','__').replace(')','__').replace('-','_')
    country_filename = path.join(countries_path, country_filename + '.md')
    country_file = open(country_filename,'w')
    country_file.write('---\nname: {:s}\nmap_url: {:s}\n---'.format(name,code))
    country_file.close()
all_countries.close()

