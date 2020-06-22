import requests

URL = 'https://api.trademe.co.nz/v1/Categories/UsedCars.json'
header = {'with_counts': True}


def test_brand_Hispano_Suiza_Not_Exist():
    r = requests.get(URL, params=header)

    ##### Check connection to API is OK #######
    assert r.status_code == 200, "API Connection error"

    brand_to_search = "Hispano Suiza’"
    ##### Check existence of the brand to search #######
    assert brand_to_search not in r.text, "Brand " + brand_to_search + " Exist"