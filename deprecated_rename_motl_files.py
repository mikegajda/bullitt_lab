import glob, os, time
from options import *
from usercheck import *

def change_file_names(options):

    search_for = options["search_for"].value
    delimiter = options["delimiter"].value
    new_column_order = options["new_column_order"].value
    
    files = sorted(glob.glob(search_for))
    assert len(files) > 0

    changes = open("motl_changes_files.csv", "a+")
    changes.write("Changes made on")

    user_check = UserCheck()
    
    for index, f in enumerate(files): #for each file, assign an index in case we need it
        old_name, extension = os.path.splitext(f)
        split_name = old_name.split(delimiter)

        assert len(split_name) == len(new_column_order)

        new_name = ""
        for col in new_column_order:
            new_name += split_name[int(col)] + delimiter
        new_name = new_name[:-1] #take off the extraneous delimiter

        if user_check.approval("Create: " + " " + new_name + extension) == True:
            new_file = open(new_name + extension, "w+")
            #os.rename(old_name + extension, new_name + extension)
            new_file.write(old_name + extension + "," +  new_name + extension + "/n")
            new_file.close()
            print "Created:", new_name + extension
        else:
            break



if __name__ == "__main__":
    #if running from the command line, execute change_header()
    default_options = Options({"search_for": StringOption(full_name="search_for", abbr="s", takes_input=True, value="Iter2*.csv"),
                                "delimiter": StringOption(full_name="delimiter", abbr="d", takes_input=True, value="_"),
                                "new_column_order": ListOption(full_name="new_column_order", abbr="o", takes_input=True, value="0,1,3,2")})
    
    change_file_names(default_options.get_user_options())
