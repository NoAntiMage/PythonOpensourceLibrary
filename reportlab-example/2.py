from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
myCanvas = canvas.Canvas('template.pdf', pagesize=letter)
width, height = letter

