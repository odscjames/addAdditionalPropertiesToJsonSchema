from addadditionalpropertiestojsonschema import add_additional_properties_to_json_schema
import os
import json

@pytest.mark.parametrize(('file_in', 'file_out'), [
    ('', ''),
])
def test_add_additional_properties_to_json_schema(file_in, file_out):

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", file_in)) as f:
        data_in = json.load(f)

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", file_out)) as f:
        data_out = json.load(f)

    

