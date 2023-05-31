import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
    
    info_trainers = requests.get(f'{host}/trainers',
                             params = {"trainer_id" : 4247})
    assert info_trainers.status_code == 200

     
def test_trainer_name():

    trainer_name = requests.get(f'{host}/trainers',
                                params = {"trainer_id" : 4247})
    assert trainer_name.json()['trainer_name'] == 'Nastya'