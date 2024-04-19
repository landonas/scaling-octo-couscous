import simplekml

kml = simplekml.Kml()
bangahz_only = kml.newpoint(name="Pathways", coords=[(21.331575, -158.065298)]) #lat, lon
#test output
print(kml.kml())
kml.save("808_bangahz_only.kml")
