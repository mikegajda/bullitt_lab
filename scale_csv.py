import glob, os, sys, getopt
from options import *
from usercheck import *


def scale_csv(options):
    search_for = options["search_for"].value
    columns_to_scale = options["columns"].value
    scale = options["scale"].value

    assert len(search_for) > 0 
    assert len(columns_to_scale) > 0
    assert scale > 0

    user_check = UserCheck()

    files = sorted(glob.glob(search_for))

    for interation_index, f in enumerate(files):
        assert f[-4:] == ".csv"
        data = [line.split(",") for line in open(f)]
        
        assert len(data) == 2

        for header_index, header in enumerate(data[0]):
            if header in columns_to_scale or header_index in columns_to_scale:
                data[1][header_index] = str(float(data[1][header_index]) * scale)

        new_file_name = "scaled" + str(scale) + f[:-4] + ".csv"

        if user_check.approval("Create " + new_file_name) == True:

            new_file = open(new_file_name, "w+")
            new_file.write(",".join(data[0]) + ",".join(data[1]))
            print("Created " + new_file_name)
            new_file.close()

        else:
            break

if __name__ == "__main__":
     #if running from the command line, execute change_header()
    default_options = Options({"search_for": StringOption(full_name="search_for", abbr="s", takes_input=True, default_value="Iter2*.csv"), 
               "columns": ListOption(full_name="columns", abbr="c", takes_input=True, default_value="xOffset,yOffset,zOffset"), 
               "scale": FloatOption(full_name="scale", abbr="x", takes_input=True, default_value="1.0")})
    
    scale_csv(default_options.get_user_options())
        
