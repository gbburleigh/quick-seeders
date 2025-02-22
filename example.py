'''
    Example usage of the seeder package
'''
from datetime import datetime, timedelta

from pprint import pprint

from seeder import Seeder
from seeder.types import (
    ID,
    Name,
    Email,
    Phone,
    Address,
    Date,
    Currency,
    Bool,
    City,
    State,
    Zip,
    Country,
    Website,
    Enum,
    Null,
    Text,
    Number
)

def schema_example():
    """Example of using JSON schema to generate data"""
    # Example schema that would come from a database or JSON file
    schema = [
        {
            "name": "id",
            "type": "integer",
            "min": 1,
            "max": 1000
        },
        {
            "name": "first_name",
            "type": "name"
        },
        {
            "name": "last_name",
            "type": "name"
        },
        {
            "name": "email",
            "type": "email",
            "email_type": "company"
        },
        {
            "name": "salary",
            "type": "currency",
            "symbol": "$",
            "min_value": 50000,
            "max_value": 150000
        },
        {
            "name": "department",
            "type": "department"
        },
        {
            "name": "hire_date",
            "type": "datetime",
            "start_date": "2020-01-01",
            "end_date": "2024-03-14"
        },
        {
            "name": "phone",
            "type": "phone"
        },
        {
            "name": "status",
            "type": "text",
            "probability": 20  # 20% chance of being empty
        },
        {
            "name": "employee_id",
            "type": "sku",
            "prefix": "EMP",
            "length": 6
        },
        {
            "name": "version",
            "type": "version",
            "major_max": 3,
            "minor_max": 15
        }
    ]

    seeder = Seeder()
    seeder.seed(schema, count=100)

    # Export seed data to different formats
    seeder.to_sql('insert_employees', 'employees')
    seeder.to_json('employees_dump')
    seeder.to_csv('employees_sheet')

    return seeder.data

def direct_generator_example():
    """Example of using generators directly"""
    seeder = Seeder()
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
    seeder.to_sql('insert_employees_direct', 'employees')
    seeder.to_json('employees_dump_direct')
    seeder.to_csv('employees_sheet_direct')

    return seeder.data

def transaction_example():
    """Generate complex financial transaction records"""

    # Calculate dates for recent transactions
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)  # Last 90 days

    schema = [
        # Transaction Identifiers
        {
            "name": "transaction_id",
            "type": "uuid",
            "version": 4
        },
        {
            "name": "reference_number",
            "type": "sku",
            "prefix": "TXN",
            "length": 12
        },
        {
            "name": "correlation_id",
            "type": "hash",
            "hash_type": "sha256"
        },

        # Temporal Data
        {
            "name": "created_at",
            "type": "datetime",
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d')
        },
        {
            "name": "processed_at",
            "type": "datetime",
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d'),
            "probability": 95  # Some might be pending
        },
        {
            "name": "settlement_date",
            "type": "datetime",
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": (end_date + timedelta(days=3)).strftime('%Y-%m-%d'),
            "probability": 90
        },

        # Financial Data
        {
            "name": "amount",
            "type": "currency",
            "min_value": 1,
            "max_value": 10000,
            "symbol": "$"
        },
        {
            "name": "fee",
            "type": "currency",
            "min_value": 0,
            "max_value": 50,
            "symbol": "$",
            "probability": 80
        },
        {
            "name": "exchange_rate",
            "type": "number",
            "probability": 30  # Only for international transactions
        },

        # Status Information
        {
            "name": "status",
            "type": "enum",
            "choices": ["completed", "pending", "failed", "reversed", "held"]
        },
        {
            "name": "risk_score",
            "type": "number",
            "min": 0,
            "max": 100,
            "probability": 95
        },
        {
            "name": "is_flagged",
            "type": "boolean",
            "probability": 5  # 5% chance of being flagged
        },

        # Customer Information
        {
            "name": "customer_id",
            "type": "uuid"
        },
        {
            "name": "customer_name",
            "type": "name"
        },
        {
            "name": "customer_email",
            "type": "email",
            "email_type": "free"
        },
        {
            "name": "customer_ip",
            "type": "ipaddress",
            "version": "ipv4"
        },
        {
            "name": "customer_country",
            "type": "country"
        },

        # Payment Method
        {
            "name": "payment_method",
            "type": "enum",
            "choices": ["credit_card", "debit_card", "bank_transfer", "crypto", "wallet"]
        },
        {
            "name": "card_last_four",
            "type": "text",
            "probability": 60  # Only for card transactions
        },
        {
            "name": "card_type",
            "type": "enum",
            "choices": ["visa", "mastercard", "amex", "discover"],
            "probability": 60
        },
        {
            "name": "bank_account_type",
            "type": "enum",
            "choices": ["checking", "savings", "business"],
            "probability": 40
        },
        {
            "name": "iban",
            "type": "iban",
            "probability": 20  # Only for international bank transfers
        },

        # Merchant Data
        {
            "name": "merchant_id",
            "type": "uuid"
        },
        {
            "name": "merchant_department",
            "type": "department"
        },
        {
            "name": "merchant_category",
            "type": "enum",
            "choices": ["retail", "food", "travel", "entertainment", "services", "technology"]
        },
        {
            "name": "merchant_country",
            "type": "country"
        },

        # Location Data
        {
            "name": "location_coordinates",
            "type": "latlng",
            "probability": 70
        },
        {
            "name": "timezone",
            "type": "timezone"
        },

        # Device Information
        {
            "name": "device_id",
            "type": "uuid",
            "probability": 85
        },
        {
            "name": "user_agent",
            "type": "useragent",
            "probability": 85
        },

        # Additional Metadata
        {
            "name": "description",
            "type": "text",
            "probability": 90
        },
        {
            "name": "notes",
            "type": "text",
            "probability": 30  # Optional notes
        },
        {
            "name": "tags",
            "type": "text",
            "probability": 40  # Optional tags
        },
        {
            "name": "version",
            "type": "version",
            "major_max": 2,
            "minor_max": 10
        },
        {
            "name": "bic",
            "type": "bic",
            "probability": 20
        },
        {
            "name": "iban",
            "type": "iban",
            "probability": 20
        },
        {
            "name": "macaddress",
            "type": "macaddress",
            "probability": 20
        },
        {
            "name": "creditcard",
            "type": "creditcard",
            "probability": 20
        },
        {
            "name": "ipaddress",
            "type": "ipaddress",
            "probability": 20
        },
        {
            "name": "latlng",
            "type": "latlng",
            "probability": 20
        },
        {
            "name": "version",
            "type": "version",
            "major_max": 2,
            "minor_max": 10
        },
        {
            "name": "sentence",
            "type": "sentence",
            "probability": 20
        }
    ]

    seeder = Seeder()
    seeder.seed(schema, count=1000)

    # Export data
    seeder.to_json('financial_transactions')
    seeder.to_csv('financial_transactions')
    seeder.to_sql('insert_transactions', 'financial_transactions')

    return seeder.data

if __name__ == '__main__':
    # Run schema example
    print("Running schema example...")
    schema_data = schema_example()
    print(f"Generated {len(schema_data)} records using schema")

    # Run direct generator example
    print("\nRunning direct generator example...")
    direct_data = direct_generator_example()
    print(f"Generated {len(direct_data)} records using direct generators")

    print("\nGenerating financial transaction records...")
    data = transaction_example()
    print(f"Generated {len(data)} transaction records")

    print("Sample transaction:")
    pprint(data[0])
