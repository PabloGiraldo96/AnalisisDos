def crearTabla(dataFrame, nombretabla): 
    archivoHTML = dataFrame.to_html()
    archivo = open(f"./tables/{nombretabla}.html", "w", encoding="utf-8")
    archivo.write('''
    <!DOCTYPE html>
    <html>
    <head>
    <title> Tablas </title>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    </head>
    <body>
    ''')
    archivo.write(archivoHTML)
    archivo.write(''' 
    </body>
    </html>                  
    ''')
    archivo.close()
    
    