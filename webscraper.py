from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
import requests
from bs4 import BeautifulSoup
from reportlab.lib.units import mm,inch



#footer
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(7*inch, 0.75 * inch, "%d" % (doc.page))
    canvas.restoreState()


#Creat Pdf
def CreateNovel(URLs):

    page = requests.get(URLs)

    soup = BeautifulSoup(page.content, 'html.parser')

    #ScrapedContent = soup.find(id = 'chr-content')

    if soup.strong != None:
        story.append(Paragraph(soup.strong.text, styleH))
    if soup.b != None:
        story.append(Paragraph(soup.b.text, styleH))
    else:
        story.append(Paragraph(soup.p.text, styleH))
    story.append(Paragraph(" ."+"<br/>",styleN))       
       
    ans = input("Black box ? confirm/ nope : ")
    
    for i in soup.find_all('p'):  #remove comment after fixing black bo error
        #i is class type
        kiko = i.get_text()
       
        woo = " "
        num = 0
        
        if ans == 'c':
            for i in kiko.split():
                num = num + 1
                if num == 1:
                    woo = i[:-1]
             
                else:
                    woo = woo + " " + i[1:-1]
            story.append(Paragraph("<br\>" + woo, styleN))    
        else:
            story.append(Paragraph("<br\>" + kiko, styleN)) 
        story.append(Paragraph(".", styleN)) 
    story.append(PageBreak())
    
    
    Urls = ""
    if soup.find(id = 'next_chap', href = True) != None:
        a = soup.find(id = 'next_chap', href = True)
        Urls = "the url"+a['href']
    
    if input("Wanna add? y/n : ") == 'y':
        CreateNovel(Urls)


    
#StylesSheet mod
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

#Create pdf novel
doc = SimpleDocTemplate(input("Name of pdf file : ")+".pdf")
URL = input("Url For scrapping pls : ")
CreateNovel(URL)
doc.build(story, onFirstPage = footer, onLaterPages = footer)
print("Story created")
