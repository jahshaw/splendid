Code to help with the 'isolated capitals' problem on GOP UGQ.  Currently, this will pre-compute the distances between all capitals and allow the user to check a set of capitals to get information on how isolated they are.

Usage:
>>> from isolation import *
    << this will take a minute or so >>
>>> check_isolation(["Canberra", "Wellington"])
(2330, 2425, 1.0407725321888412, True)
>>> check_isolation(["Canberra", "Wellington", "Tarawa", "Yaren District", "Majuro"])
(2330, 1249, 0.5360515021459228, False)


The parameters returned are:
- 'Bond distance' of the set
- 'Isolation distance' of the set (i.e. what we're trying to maximise for the first part)
- 'Relative isolation' of the set (i.e. what we're trying to maximise for the second part)
- Whether the set is actually 'isolated' at all

Notes:
- Written and tested using Python 3.6, I have no idea whether this works on earlier versions.
- This requires the 'geopy' module to calculate distances (use pip install to get it).  Geopy uses a WGS84 spheroid projection so the inter-capital distances are slightly different than those calculated by Bilen on the UGQ spreadsheet (by up to about 0.5%).  However, Jon Lawn has confirmed this doesn't change any answers.
