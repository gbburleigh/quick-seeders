'''
    Test the seeder package
'''
from seeder import Seeder
from seeder.types import (
    ID,
    Name,
    Email,
    Phone,
    Address,
    Date,
    Datetime,
    Time,
    Timestamp,
    TimeZone,
    DayOfWeek,
    Color,
    JobTitle,
    CompanyDepartment,
    FileExtension,
    SocialMediaHandle,
    IPAddress,
    LatitudeLongitude,
    Version,
    Sentence,
    Paragraph,
    UserAgent,
    Hash,
    ISBN,
    ISBN13,
    EAN,
    SKU,
    MACAddress,
    CreditCardNumber,
    IBAN,
    BIC
)

def test_seeder_initialization():
    '''
        Test the seeder initialization
    '''
    seeder = Seeder()
    assert isinstance(seeder, Seeder)
    assert seeder.data == {}

def test_basic_seed():
    '''
        Test the basic seed
    '''
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
    '''
        Test the direct generators
    '''
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
    '''
        Test the export formats
    '''
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

def test_complex_schema_from_generators():
    '''
        Test a complex schema from generators
    '''
    seeder = Seeder()
    generators = [
        ID('id'),
        Name('first_name'),
        Email('email'),
        Phone('phone'),
        Address('address'),
        Date('date'),
        Datetime('datetime'),
        Time('time'),
        Timestamp('timestamp'),
        TimeZone('timezone'),
        DayOfWeek('day_of_week'),
        Color('color'),
        JobTitle('job_title'),
        CompanyDepartment('company_department'),
        FileExtension('file_extension'),
        SocialMediaHandle('social_media_handle'),
        IPAddress('ip_address'),
        LatitudeLongitude('latitude_longitude'),
        Version('version'),
        Sentence('sentence'),
        Paragraph('paragraph'),
        UserAgent('user_agent'),
        Hash('hash'),
        ISBN('isbn'),
        ISBN13('isbn13'),
        EAN('ean'),
        SKU('sku'),
        MACAddress('mac_address'),
        CreditCardNumber('credit_card_number'),
        IBAN('iban'),
        BIC('bic')
    ]

    result = seeder.seed(generators, count=5)

    assert len(result) == 5
    assert all("id" in record for record in result)
