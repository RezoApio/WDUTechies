def checkio(data):
   
    #replace this for solution

    #Extracting points coordinates from data string
    #Assuming 1 digit values only
    x1=int(data[1])
    y1=int(data[3])
    x2=int(data[7])
    y2=int(data[9])
    x3=int(data[13])
    y3=int(data[15])

    print(str(x1)+";"+str(y1)+";"+str(x2)+":"+str(y2)+";"+str(x3)+";"+str(y3))


    #Calculus extracted from https://cral.univ-lyon1.fr/labo/fc/Ateliers_archives/ateliers_2005-06/cercle_3pts.pdf

    xc=((x3**2-x2**2+y3**2-y2**2)/(2*(y3-y2))-(x2**2-x1**2+y2**2-y1**2)/(2*(y2-y1)))/((x2-x1)/(y2-y1)-(x3-x2)/(y3-y2))
    print((x3**2-x2**2+y3**2-y2**2)/(2*(y3-y2)))
    print((x2**2-x1**2+y2**2-y1**2)/(2*(y2-y1)))
    print(xc)
    
    ##-((x2**2-x1**2+y2**2-y1**2)/2*(y2-y1)))/(((x2-x1)/(y2-y1))-((x3-x2)/(y3-y2)))
    yc=((x2**2-x1**2+y2**2-y1**2)/2*(y2-y1))-((x2-x1)/(y2-y1))*xc
    print(yc)
    Rc=((x1-xc)**2+(y1-yc)**2)**(1/2)

    #Rounding results

    xc=round(xc,2)
    yc=round(yc,2)
    Rc=round(Rc,2)
    
    res="(x-"+str(xc)+")^2+(y-"+str(yc)+")^2="+str(Rc)+"^2"
    print(res)
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
   




