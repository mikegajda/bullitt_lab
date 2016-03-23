import glob, os, time, shutil
from options import *
from usercheck import *
from log import *

def change_file_names(options):

    search_for = options["search_for"].value
    delimiter = options["delimiter"].value
    new_column_order = options["new_segment_order"].value
    user_approval_required = options["user_approval_required"].value
    write_changes_file_option = options["write_changes_file"].value
    verbose_option = options["verbose"].value
    
    files = sorted(glob.glob(search_for))
    assert len(files) > 0

    log = Log(script_name="change_file_names", write_changes=write_changes_file_option, verbose=verbose_option)
    log.send("running in {0}".format(os.getcwd()))

    user_check = UserCheck(user_approval_required)

    for index, f in enumerate(files): #for each file, assign an index in case we need it
        old_name, extension = os.path.splitext(f)
        split_name = old_name.split(delimiter)

        #assert len(split_name) == len(new_column_order)

        new_name = ""
        for col in new_column_order:
            new_name += split_name[int(col)] + delimiter
        new_name = new_name[:-1] #take off the extraneous delimiter

        if user_check.approval("Create: " + " " + new_name + extension) == True:
            #os.rename(old_name + extension, new_name + extension)
            shutil.copy(old_name + extension, new_name + extension)
            log.send("Created: {0}{1}".format(new_name, extension))
            log.change("{0},{1}".format(old_name + extension, new_name + extension))
        else:
            log.send("approval not granted, exiting")
            break

    return log.finish()


if __name__ == "__main__":
    #if running from the command line, execute change_header()
    default_options = Options({"search_for": StringOption(full_name="search_for", abbr="s", takes_input=True, default_value="Iter2*.csv"),
                                "delimiter": StringOption(full_name="delimiter", abbr="d", takes_input=True, default_value="_"),
                                "new_segment_order": ListOption(full_name="new_segment_order", abbr="o", takes_input=True, default_value="0,1,3,2"),
                                "rename_current_file": BoolOption(full_name="rename_current_file", abbr="r", takes_input=False, default_value="False"),
                                "user_approval_required": BoolOption(full_name="user_approval_required", abbr="a", takes_input=False, default_value="True"),
                                "write_changes_file": BoolOption(full_name="write_changes_file", abbr="w", takes_input=False, default_value="True"),
                                "verbose": BoolOption(full_name="verbose", abbr="v", takes_input=False, default_value="True")})
    
    change_file_names(default_options.get_user_options())
