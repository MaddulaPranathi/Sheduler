import re
from datetime import datetime
def parse_input(user_input):
    match=re.match(r"remind me to (.+) at (\d{1,2}:\d{2})",user_input.lower())
    if match:
        task=match.group(1)
        time_str=match.group(2)
        return task,time_str
    return None,None