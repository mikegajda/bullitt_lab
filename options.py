import getopt, sys, os
class StringOption:
    def __init__(self, full_name, abbr, takes_input, default_value=None):
        assert isinstance(full_name, str)
        assert isinstance(abbr, str)
        assert isinstance(takes_input, bool)

        self.value = default_value
        
        self.full_name = full_name
        self.abbr = abbr
        self.takes_input = takes_input
        self.retrieval_short = "-" + abbr
        self.retrieval_long = "--" + full_name

        if self.takes_input == True:
            self.short_opt = abbr + ":"
        else:
            self.short_opt = abbr

        self.long_opt = full_name + "="
    
    def __str__(self):
        return str((self.full_name, self.abbr, self.takes_input, self.value))
    
    def __repr__(self):
        return self.__str__()

    def set_value(self, new_value):
        self.value = new_value

class ListOption(StringOption):

    def __init__(self, *args, **kwargs):
        StringOption.__init__(self, *args, **kwargs)
        self.value = self.value.split(",")

    def set_value(self, new_value):
        self.value = new_value.split(",")

class IntOption(StringOption):

    def __init__(self, *args, **kwargs):
        StringOption.__init__(self, *args, **kwargs)
        self.value = int(self.value)

    def set_value(self, new_value):
        self.value = int(new_value)

class FloatOption(StringOption):

    def __init__(self, *args, **kwargs):
        StringOption.__init__(self, *args, **kwargs)
        self.value = float(self.value)

    def set_value(self, new_value):
        self.value = int(new_value)

class BoolOption(StringOption):

    def __init__(self, *args, **kwargs):
        StringOption.__init__(self, *args, **kwargs)
        if self.value == "True":
            self.value = True
        elif self.value == "False":
            self.value = False
        elif self.value == "1":
            self.value = True
        elif self.value == "0":
            self.value = False
        else:
            raise ValueError("Unsupported boolean value passed in")

    def set_value(self, new_value):
        self.value = not self.value

class Options:

    def __init__(self, options):
        self.options = options

    def __getitem__(self, key):
        return self.options[key]

    def print_options(self):
        print "The following options have been set:"
        for option in self.options:
            print self.options[option].full_name, "=", self.options[option].value
        print "\n"
    def get_user_options(self):
        options_long_list = [self.options[option].long_opt for option in self.options]
        options_short_list = "".join([self.options[option].short_opt for option in self.options])
        #print "running in:", os.path.dirname(os.path.realpath(sys.argv[0]))
        print "running in:", os.getcwd()
        try:
            retrieved_opts, args = getopt.getopt(sys.argv[1:], options_short_list, options_long_list)
        except getopt.GetoptError as error:
            print error
            sys.exit()
            
        for option in self.options:
            for retrieved_opt in retrieved_opts:
                retrieved_opt_name, retrieved_value = retrieved_opt
                if (self.options[option].retrieval_long == retrieved_opt_name) or (self.options[option].retrieval_short == retrieved_opt_name):
                    self.options[option].set_value(retrieved_value)

        self.print_options()

        return self.options