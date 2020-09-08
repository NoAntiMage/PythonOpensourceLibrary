import dominate
from dominate.tags import *

print(
html(
    body(
        h1('Hello wuji')
    )
))

test = label(cls='classname anothername', fr='someinput')
someinputtest = label(_class='classname anothername', _for='someinput')
print(test)

test1 = div(data_employee='10086')
print(test1)

header = div()
header['id'] = 'header'
print(header)