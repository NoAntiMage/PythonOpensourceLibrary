import dominate
from dominate.tags import *

doc = dominate.document(title='Hello wujimaster')

with doc.head:
    link(rel='stylesheet',href='/d/wuji_workstation/code_repo/hello_boostrap/bootstrap-4.5.0-dist/css/bootstrap.min.css')
    script(rel='text/javascript',src='/d/wuji_workstation/code_repo/hello_boostrap/bootstrap-4.5.0-dist/js/bootstrap.min.js')
    script(rel='text/javascript',src='/d/wuji_workstation/code_repo/hello_boostrap/jquery-3.4.1/jquery-3.4.1.min.js')

with doc:
    with(div(id='header').add(ol())):
        for i in ['home', 'about', 'contact']:
            li(a(i.title(), href='/{}.html'.format(i)))

    with div():
        attr(cls='body')
        p('hello wuji.')


print(doc)

