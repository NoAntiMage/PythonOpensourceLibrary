from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import pink, black, red, blue, green


def coords(c):
    c.setStrokeColor(pink)
    c.grid([inch, 2*inch,3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(black)
    c.setFont("Times-Roman", 20)
    c.drawString(0,0, "(0,0) the Origin")
    c.drawString(2.5*inch, inch, "(2.5,1) in inches")
    c.drawString(4*inch, 2.5*inch, "(4, 2.5)")
    c.setFillColor(red)
    c.rect(0, 0.2*inch, 0.2*inch, 0.3*inch, fill=1)
    c.setFillColor(green)
    c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)


def form_pdf(c):
    c.showPage()
    c.save()


if __name__ == '__main__':
    c = canvas.Canvas('hello.pdf')
    coords(c)
    form_pdf(c)
