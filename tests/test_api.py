# from app import api


def test_is_location():
    test_input = ['DIO PORCO', 'GESU']
    test_output = api.transform(test_input)
    assert test_output

    # resp_db = client.get('/sources')
    # sources = resp_db.get_json()['data']
    # assert sources == ['AMR', 'FAO', 'ES']
    #
    # resp_no_db = client.get('/src')
    # assert resp_no_db.status_code == 404
