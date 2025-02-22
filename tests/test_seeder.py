import pytest
from seeder import Seeder
from seeder.types import *

def test_seeder_initialization():
    seeder = Seeder()
    assert isinstance(seeder, Seeder)
    assert seeder.data == {}

def test_basic_seed():
    seeder = Seeder()
    schema = [
        {
            "name": "id",
            "type": "integer",
            "min": 1,
            "max": 10
        },
        {
            "name": "name",
            "type": "name"
        }
    ]
    
    result = seeder.seed(schema, count=1)
    assert len(result) == 1
    assert "id" in result[0]
    assert "name" in result[0]
    assert isinstance(result[0]["id"], int)
    assert isinstance(result[0]["name"], str)

def test_direct_generators():
    seeder = Seeder()
    generators = [
        ID('id'),
        Name('first_name'),
        Email('email')
    ]
    
    result = seeder.seed(generators, count=5)
    assert len(result) == 5
    assert all("id" in record for record in result)
    assert all("first_name" in record for record in result)
    assert all("email" in record for record in result)
    assert all("@" in record["email"] for record in result)

def test_export_formats():
    seeder = Seeder()
    schema = [{"name": "test", "type": "text"}]
    seeder.seed(schema, count=1)
    
    # Test JSON export
    json_path = seeder.to_json('test_export')
    assert json_path.endswith('.json')
    
    # Test CSV export
    csv_path = seeder.to_csv('test_export')
    assert csv_path.endswith('.csv')
    
    # Test SQL export
    sql_path = seeder.to_sql('test_export', 'test_table')
    assert sql_path.endswith('.sql') 