import requests

URL = 'https://api.trademe.co.nz/v1/Categories/UsedCars.json'

def test_brands_availables():
    r = requests.get(URL)
    ##### Check connection to API is OK #######
    assert r.status_code == 200, "API Connection error"
    ##### Format the response to JSON. Now we can work with the JSON response ######
    r = r.json()
    total_brands = len(r["Subcategories"])
    print("Total Brands", total_brands)