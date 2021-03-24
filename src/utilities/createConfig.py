# import module
import configparser

# create configparser object
config_file = configparser.ConfigParser()

# define sections and their key and value pairs
config_file["Filenames"] = {
    # the script expect the input file to be in the local folder
    "input-file" : "foreman_cif.mov",
    # the script will create automatically the output file in the local folder
    "output-file" : "output-foreman_cif"
}

config_file["Parameters"] = {
    "Macroblock-dimension" : "16",
    "Temporal-displacement" : "2"
}

#Write the above sections to config.ini file
with open('./src/config.ini', 'w') as conf:
    config_file.write(conf)