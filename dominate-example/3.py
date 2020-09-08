import dominate
from dominate.tags import *

l = ul()
for item in range(4):
    l += li('Item #', item)

print(l)

menu_items = {'Home': '/home/', 'About': '/about/', 'Downloads': '/downloads/', 'Links': '/links/'}


print(
        ul(
            li(
                a(name, href=link,__pretty=False) for (name, link) in menu_items.items()
            )
        )
    )

_html = html()
_body = _html.add(body())
header = _body.add(div(id='header'))
content = _body.add(div(id='content'))
footer = _body.add(div(id='footer'))
print(_html)

_html = html()
_head, _body = _html.add(head(title('Hello wuji')), body())
names = ['header', 'content', 'footer']
header, content, footer = _body.add([div(id=name) for name in names])
print(_html)

header = div()
header['id'] = 'header'
print(header)


header = div('Test')
header[0] = 'Hello World'
print(header)

print(comment('COMMENTS'))

bar = div(span('Hello wuji'))
print(bar.render())

h = ul()
with h:
    li('One')
    li('Two')
    li('Three')
print(h)

h = html()
with h.add(body()).add(div(id='content')):
    h1('Hello wuji')
    p('i am a paragraph')
    with table().add(tbody()):
        l = tr()
        l += td('One')
        l.add(td('Two'))
        with l:
            td('Three')
print(h)

d = div()
with d:
    attr(id='header')
print(d)

from dominate.util import text
para = p(__pretty=False)
with para:
    text('Have a look at our ')
    a('other products', href='/products')
print(para)


def greeting(name):
    with div() as d:
        p('Hello, %s' %name)
    return d
print(greeting('wuji'))

@div
def greeting(name):
    p('Hello %s' %name)
print(greeting('wuji'))


@div(h2('Welcome'), cls='greeting')
def greeting(name):
    p('Hello %s' % name)

print(greeting('Bob'))


d =  dominate.document()
print(d)