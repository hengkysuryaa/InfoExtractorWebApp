def nearestNum(listangka,posKeyword,kal):
    nearposAng = -1
    nearAng = ''
    for ang in listangka:
        ang.replace(' ','')
        posAng = kal.rfind(ang,0,posKeyword)
        if (posAng > nearposAng):
            nearAng = ang
            nearposAng = posAng
    return kal[nearposAng:(nearposAng+len(nearAng))].replace(' ','')