import json
from seeder import Seeder
from seeder.types import *

# Create seeder instance
seeder = Seeder()

# Generate seed data with generics
seeder.seed([
    ID('id'),
    Name('first_name'),
    Name('last_name'),
    Email('email'),
    Phone('phone'),
    Address('address'),
    City('city'),
    State('state'),
    Zip('zip'),
    Country('country'),
    Website('website'),
    Enum('gender', ['male', 'female', 'other']),
    Currency('salary', min_value=1000, max_value=100000, probability=50),
    Date('birth_date'),
    Date('hire_date'),
    Date('start_date'),
    Date('end_date'),
    Text('description', probability=50),
    Number('age'),
    Bool('is_active'),
    Bool('is_deleted'),
    Bool('is_verified'),
    Bool('is_suspended'),
    Bool('is_blocked'),
    Null('partner_id', ID('partner_id'), probability=50),
], count=100)

# Export seed data to different formats
seeder.to_sql('insert_employees', 'employees')
seeder.to_json('employees_dump')
seeder.to_csv('employees_sheet')

# Use seed data in memory
result = seeder.data