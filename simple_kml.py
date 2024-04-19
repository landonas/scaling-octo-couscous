import simplekml

kml = simplekml.Kml()
bangahz_only = kml.newpoint(name="Pathways", coords=[( -158.065, 21.331)]) 
bangahz_only.style.labelstyle.color = "ff0000ff"
bangahz_only.style.iconstyle.href='http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png'
#test output
#print(kml.kml())
kml.save("808_bangahz_only.kml")
