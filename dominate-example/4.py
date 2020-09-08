import dominate
from dominate.tags import *

doc = dominate.document(title='Hello wujimaster')

with doc.head:
    link(rel='stylesheet',href='../../hello_boostrap/bootstrap-4.5.0-dist/css/bootstrap.min.css')
    script(rel='text/javascript',src='../../hello_boostrap/bootstrap-4.5.0-dist/js/bootstrap.min.js')
    script(rel='text/javascript',src='../../hello_boostrap/jquery-3.4.1/jquery-3.4.1.min.js')

with doc.body:
    h1('Hello world, wuji!')
    container = div(cls='container')
    jumbtron = div(cls='jumbotron')
    container.add(jumbtron)
    jumbtron.add(h1('you are at container'))
    jumbtron.add(p('check the demo'))
    row = div(cls='row')
    container.add(row)
for i in range(3):
    with row.add(div(cls='col-sm-4')):
        h1('Column %d' %i)

print(doc)
