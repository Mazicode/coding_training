from address_parser import Parser
import re
from json import JSONEncoder

mixed_inputs = ["55.674146, 12.569553", "H. C. Andersens Blvd. 27, 1553 København V, Denmark", "37.423021, -122.083739",
                "1600 Amphitheatre Parkway, Mountain View, CA"]

coord_regex = '^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'

parser = Parser()


def is_location(input):
    adr = parser.parse(input)
    if adr.road.dict['name'] and adr.road.dict['suffix'] \
            and adr.locality.dict['city']:
        return True


def is_coordinates(input):
    coord = re.findall(coord_regex, input)
    if coord:
        return True


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
