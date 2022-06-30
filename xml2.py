# ProjetXML.py
#We can import this data by reading from a file:
from lxml import etree
doc=etree.parse('movies.xml')
import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
#preparation du desktop app
from PyQt5.QtWidgets import *
app = QApplication([])
window = QMainWindow()
screen = QWidget()
layout = QGridLayout()
screen.setLayout(layout)
window.setCentralWidget(screen)
window.setWindowTitle('Projet XML')

def RechTitre():
    valR,rech  = QInputDialog.getText(
        window, 
        'Recherche Par Titre',
        'Donner le Titre :'# parent widget
        )
    for movie in root.iter("./genre/decade/movie[@title='{}']".format(valR)):
        print(movie.attrib)
def RechYear() :
    year,rech1  = QInputDialog.getText(
        window, 
        'Recherche par Anné',
        'Anné :'# parent widget
        )
    for movie in root.findall("./genre/decade/movie/[year='{}']".format(year)):
        print(movie.attrib)
def RechType() :
    valType,rech2  = QInputDialog.getText(
        window, 
        'Recherche par Type',
        'Type :'# parent widget
        )
    for movie in root.findall("./genre/decade/movie/[format='{}']".format(valType)):
        print(movie.attrib)
def RechRg() :
    valrg,rech3  = QInputDialog.getText(
        window, 
        'Recherche par Rang',
        'Anné :'# parent widget
        )
    for movie in root.findall("./genre/decade/movie/[rating='{}']".format(valrg)):
        print(movie.attrib)

def suppmovie() :
    valsup,sup  = QInputDialog.getText(window, 'Supprimer','Element à Supprimer'# parent widget
        )
    elem1 = doc.find("./genre/decade/movie[@title='{}']".format(valsup))
    parent = elem1.getparent()
    parent.remove(elem1)
    print(etree.tostring(doc))
    doc.write("movies.xml")

def suppgenre() :
    valsuppgenre,sup  = QInputDialog.getText(window, 'Supprimer Genre','Genre à Supprimer'# parent widget
        )
    elem = doc.find("./genre[@category='{}']".format(valsuppgenre))
    parent = elem.getparent()
    parent.remove(elem)
    print(etree.tostring(doc))
    doc.write("movies.xml")

    #elemsup = root.find("./genre[@category='{}']".format(valsuppgenre))
    #titsup = root.find("./genre[@category='Action']/decade[@years='1990s']")
    #dec.remove(elemsup)


    
def ajout() :
    valgenre,genre  = QInputDialog.getText(window, 'Category','Genre'# parent widget
        )
    valyear ,yr  = QInputDialog.getText(window, 'Year','Anné'# parent widget
      )
    valdecade ,decade  = QInputDialog.getText(window,'Decade','Decade' # parent widget
     )
    valtitre, titre  = QInputDialog.getMultiLineText( window, 'Titre' ,'Nom film',# parent widget
   )
    valfavorie, favorie  = QInputDialog.getText(window, 'Favorie' ,'True/False',# parent widget
   )
    valmult, mult  = QInputDialog.getText(window, 'Multiple' ,'Yes/No',# parent widget
   )
    valformat,formate  = QInputDialog.getText(window, 'Format' ,'DVD/Online',# parent widget
   )
    valrating ,rating  = QInputDialog.getText( window, 'Rating' ,'donner le rating',# parent widget
   )

    valdesc ,desc = QInputDialog.getMultiLineText(window, 'Description' ,'Ecrire une petite description',# parent widget
)
    genre = ET.SubElement(root, "genre")
    #root.append (genre)
    #status = root.find('.//genre')
    genre.attrib['category'] = '{}'.format(valgenre)

    
    decade = ET.SubElement(genre, "decade")
    #status = root.find('.//decade')
    decade.attrib['years'] = '{}'.format(valdecade)
    
    movie = ET.SubElement(decade, "movie")
    #b2.text = "6999"
    movie.attrib['title'] = '{}'.format(valtitre)
    #status = root.find('.//movie')
    #status.attrib['favorite'] = '{}'.format(valfavorite)

    form = ET.SubElement(movie , "format")
    form.text = "{}".format(valformat)
    #status = root.find('.//format')
    form.attrib['multiple'] = '{}'.format(valmult)


    year = ET.SubElement(movie , "year")
    year.text = "{}".format(valyear)

    rg = ET.SubElement(movie , "rating")
    rg.text = "{}".format(valrating)

    des = ET.SubElement(movie , "description")
    des.text = "{}".format(valdesc)
    print(ET.tostring(root))
    tree.write("movies.xml")


def modify() :
    elem,element  = QInputDialog.getText(
        window, 
        'Corriger',
        'Entrer l''element à Corriger'# parent widget
        )
    nv,nvelement  = QInputDialog.getText(
        window, 
        'Corriger',
        'Entrer le nouvelle Titre'# parent widget
        )
    b2tf = root.find("./genre/decade/movie[@title='{}']".format(elem))
    #print(b2tf)
    b2tf.attrib["title"] = "{}".format(nv)
    #print(b2tf.attrib)
    tree.write("movies.xml")
    #tree = ET.parse('movies.xml')
    #root = tree.getroot()
    
# Create a new XML file with the results



button1 = QPushButton()
button1.setText('Supprimer Movie')
button1.clicked.connect(suppmovie)
layout.addWidget(button1, 1,0, 1, 2)

button8 = QPushButton()
button8.setText('Supprimer Genre')
button8.clicked.connect(suppgenre)
layout.addWidget(button8, 2,0, 1, 2)

button2 = QPushButton()
button2.setText('Ajouter')
button2.clicked.connect(ajout)
layout.addWidget(button2, 3, 0, 1, 2)

button3 = QPushButton()
button3.setText('Modifier')
button3.clicked.connect(modify)
layout.addWidget(button3, 4, 0, 1, 2)

button4 = QPushButton()
button4.setText('Chercher Par Titre')
button4.clicked.connect(RechTitre)
layout.addWidget(button4, 1, 3, 1, 2)


button5 = QPushButton()
button5.setText('Chercher Par Anné')
button5.clicked.connect(RechYear)
layout.addWidget(button5, 2, 3, 1, 2)

button6 = QPushButton()
button6.setText('Chercher Par Type')
button6.clicked.connect(RechType)
layout.addWidget(button6, 3, 3, 1, 2)

button7 = QPushButton()
button7.setText('Chercher Par Rang')
button7.clicked.connect(RechRg)
layout.addWidget(button7, 4, 3, 1, 2)






window.setMinimumSize(500, 200)
window.show()

tree.write("movies.xml")
tree = ET.parse('movies.xml')
root = tree.getroot()

app.exec_()


