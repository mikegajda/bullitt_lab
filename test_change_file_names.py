import os, pytest
from options import *
from change_file_names import *

test_cases = ["segment1_segment2_segment3.csv", "segment1-segment2-segment3.csv"]

def test_change_file_names_1(test_case=test_cases[0]):
	f = open(test_case, "w+")
	f.write("test_content")
	f.close()

	options = Options({"search_for": StringOption(full_name="search_for", abbr="s", takes_input=True, default_value=test_case),
                                "delimiter": StringOption(full_name="delimiter", abbr="d", takes_input=True, default_value="_"),
                                "new_segment_order": ListOption(full_name="new_segment_order", abbr="o", takes_input=True, default_value="0,2,1"),
                                "rename_current_file": BoolOption(full_name="rename_current_file", abbr="r", takes_input=False, default_value="False"),
                                "user_approval_required": BoolOption(full_name="user_approval_required", abbr="a", takes_input=False, default_value="False"),
                                "write_changes_file": BoolOption(full_name="write_changes_file", abbr="w", takes_input=False, default_value="False"),
                                "verbose": BoolOption(full_name="verbose", abbr="v", takes_input=False, default_value="True")})


	output_file = change_file_names(options)

	f = open(test_case, "r")

	assert f.read() == "test_content"
	f.close()
	assert os.path.isfile("segment1_segment3_segment2.csv") == True


	assert os.path.isfile(output_file) == True


	os.remove(test_case)
	os.remove("segment1_segment3_segment2.csv")
	os.remove(output_file)


def test_change_file_names_2(test_case=test_cases[1]):
	f = open(test_case, "w+")
	f.write("test_content")
	f.close()

	options = Options({"search_for": StringOption(full_name="search_for", abbr="s", takes_input=True, default_value=test_case),
                                "delimiter": StringOption(full_name="delimiter", abbr="d", takes_input=True, default_value="-"),
                                "new_segment_order": ListOption(full_name="new_segment_order", abbr="o", takes_input=True, default_value="0,2,1"),
                                "rename_current_file": BoolOption(full_name="rename_current_file", abbr="r", takes_input=False, default_value="False"),
                                "user_approval_required": BoolOption(full_name="user_approval_required", abbr="a", takes_input=False, default_value="False"),
                                "write_changes_file": BoolOption(full_name="write_changes_file", abbr="w", takes_input=False, default_value="False"),
                                "verbose": BoolOption(full_name="verbose", abbr="v", takes_input=False, default_value="True")})


	output_file = change_file_names(options)

	f = open(test_case, "r")

	assert f.read() == "test_content"
	f.close()
	assert os.path.isfile("segment1-segment3-segment2.csv") == True

	assert os.path.isfile(output_file) == True


	os.remove(test_case)
	os.remove("segment1-segment3-segment2.csv")
	os.remove(output_file)


