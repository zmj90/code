"""

"""

import re


list_result = re.findall("(梦幻|王者)\w*","王者荣耀、刺激战场、梦幻西游")
print(list_result) #  ['王者', '梦幻']

list_result = re.findall("(?:梦幻|王者)\w*","王者荣耀、刺激战场、梦幻西游")
print(list_result) #  ['王者荣耀', '梦幻西游']
