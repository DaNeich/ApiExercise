import requests

URL = 'https://api.trademe.co.nz/v1/Categories/UsedCars.json'
header = {'with_counts': True}

def test_search_brand_Kia_and_count():
    r = requests.get(URL, params=header)

    ##### Check connection to API is OK #######
    assert r.status_code == 200, "API Connection error"

    brand_to_search = "Kia"
    ##### Check existence of the brand to search #######
    assert brand_to_search in r.text, "Brand " + brand_to_search + " Does not Exist"

    ##### parse response to json to work as array #####
    r = r.json()
    # I get the value of 'count', to know how many 'brand_to_search' vehicles are available to sell.
    x = 0
    while x < len(r["Subcategories"]) - 1:
        if r["Subcategories"][x]["Name"] == brand_to_search:
            print("There are", r["Subcategories"][x]['Count'], r["Subcategories"][x]["Name"], "vehicles to sell")
            pass
            break
        x = x + 1