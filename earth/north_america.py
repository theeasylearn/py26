def getCountries():
    north_american_countries = ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"]
    return north_american_countries

def hasCountry(country):
    #if country exist in asia it should return True otherwise it should return false 
    list = getCountries()
    if country in list:
        return True 
    else:
        return False 