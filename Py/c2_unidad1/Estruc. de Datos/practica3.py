articulos = {
    
}
sol = "si"
while sol == 'si':
    arts = str(input('Ingresa el nombre del articulo: '))
    pres = int((input('Ingresa el presio del articulo: ')))
    articulos.update({pres:arts})
    sol = input('Quieres seguir agregando si/no ')
    
articulos_ord = dict(sorted(articulos.items(), reverse=True)) 
primer = (next(iter(articulos_ord)))
val = articulos_ord[primer]
print('el articulo mas caro es:',val)
print('con un valor de:',primer)
iva = ((primer * 16)/100)
total = (iva + primer)
print('El precio total con iva es de:', total)