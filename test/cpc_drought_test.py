import pandas

import ulmo

import test_util


test_sets = [
    {
    'filename': 'cpc/drought/palmer94',
    'start': '1995-02-19',
    'end': '1995-02-25',
    'state': 'NC',
    'climate_division': 4,
    'values': [{
        'cmi': 1.92,
        'pdsi': 0.88,
        'period': '1995-02-19/1995-02-25',
        'potential_evap': 0.17,
        'precipitation': 0.1,
        'runoff': 0.0,
        'soil_moisture_lower': 5.0,
        'soil_moisture_upper': 0.93,
        'temperature': 47.0
        }]
    },
    {
    'filename': 'cpc/drought/palmer99',
    'start': '1999-07-25',
    'end': '1999-07-31',
    'state': 'TX',
    'climate_division': 3,
    'values': [{
        'cmi': -2.31,
        'pdsi': -1.37,
        'period': '1999-07-25/1999-07-31',
        'potential_evap': 1.75,
        'precipitation': 0.0,
        'runoff': 0.0,
        'soil_moisture_lower': 1.68,
        'soil_moisture_upper': 0.0,
        'temperature': 87.0
        }]
    },
    {
    'filename': 'cpc/drought/palmer10',
    'start': '2010-5-20',
    'end': '2010-6-13',
    'state': 'AL',
    'climate_division': 1,
    'values': [{
        'cmi': 0.05,
        'pdsi': 0.53,
        'period': '2010-06-06/2010-06-12',
        'potential_evap': 1.37,
        'precipitation': 0.71,
        'runoff': 0.0,
        'soil_moisture_lower': 4.86,
        'soil_moisture_upper': 0.0,
        'temperature': 77.6
        }]
    },
]


def test_get_data_by_state():
    for test_set in test_sets:
        with test_util.mocked_requests(test_set['filename']):
            data = ulmo.cpc.drought.get_data(state=test_set['state'], start=test_set['start'],
                end=test_set['end'])
        assert len(data) == 1
        assert test_set['state'] in data


def test_get_data():
    for test_set in test_sets:
        with test_util.mocked_requests(test_set['filename']):
            data = ulmo.cpc.drought.get_data(start=test_set['start'], end=test_set['end'])

        values = data.get(test_set['state'], {}).get(test_set['climate_division'])
        test_values = test_set['values']

        for test_value in test_values:
            assert test_value in values


def test_get_data_as_dataframe():
    with test_util.mocked_requests('cpc/drought/palmer10'):
        data = ulmo.cpc.drought.get_data(start='2010-5-20', end='2010-6-13',
                as_dataframe=True)

        assert isinstance(data, pandas.DataFrame)
