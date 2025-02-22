'''
    Test each seeder type
'''
from datetime import datetime

import pytest

from seeder.types import (
    Text,
    Number,
    Email,
    Null,
    Enum,
    Date,
    Currency,
    Bool,
    Int,
    Datetime,
    Time,
    Timestamp,
    TimeZone,
    DayOfWeek,
    UUID,
    Color,
    JobTitle,
    CompanyDepartment,
    FileExtension,
    SocialMediaHandle,
    IPAddress,
    LatitudeLongitude,
    Version,
    URL,
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

def test_text_type():
    '''
        Test the Text type
    '''
    text = Text("test_column")
    result, name = text()
    assert name == "test_column"
    assert isinstance(result, str)

def test_number_type():
    '''
        Test the Number type
    '''
    number = Number("test_number")
    result, name = number()
    assert name == "test_number"
    assert isinstance(result, (int, float))

def test_email_type():
    '''
        Test the Email type
    '''
    # Test default email
    email = Email("test_email")
    result, name = email()
    assert name == "test_email"
    assert "@" in result
    assert "." in result

    # Test different email types
    email_types = ["safe", "free", "company"]
    for email_type in email_types:
        email = Email("test_email", email_type=email_type)
        result, name = email()
        assert "@" in result
        assert "." in result

    # Test specific domain
    email = Email("test_email", email_type="specific", domain="example.com")
    result, name = email()
    assert result.endswith("@example.com")

def test_null_type():
    '''
        Test the Null type
    '''
    # Test with no value
    null = Null("test_null")
    result, name = null()
    assert name == "test_null"
    assert result is None

    # Test with fallback value
    null_with_fallback = Null("test_null", value="fallback")
    result, name = null_with_fallback()
    assert result == "fallback"

def test_enum_type():
    '''
        Test the Enum type
    '''
    choices = ["A", "B", "C"]
    enum = Enum("test_enum", choices)
    result, name = enum()
    assert name == "test_enum"
    assert result in choices

def test_date_type():
    '''
        Test the Date type
    '''
    date = Date("test_date")
    result, name = date()
    assert name == "test_date"
    assert isinstance(result, str)
    # Could add more specific date format validation

def test_currency_type():
    '''
        Test the Currency type
    '''
    currency = Currency("test_currency", symbol="$", min_value=10, max_value=20)
    result, name = currency()
    assert name == "test_currency"
    assert result.startswith("$")
    value = float(result.replace("$", ""))
    assert 10 <= value <= 20

def test_bool_type():
    '''
        Test the Bool type
    '''
    bool_type = Bool("test_bool")
    result, name = bool_type()
    assert name == "test_bool"
    assert result is not None

def test_int_type():
    '''
        Test the Int type
    '''
    int_type = Int("test_int")
    result, name = int_type()
    assert name == "test_int"
    assert isinstance(result, int)

def test_datetime_type():
    '''
        Test the Datetime type
    '''
    datetime_type = Datetime("test_datetime")
    result, name = datetime_type()
    assert name == "test_datetime"
    assert isinstance(result, str)
    # Verify it's a valid datetime string
    try:
        datetime.strptime(result, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        pytest.fail("Invalid datetime format")

def test_time_type():
    '''
        Test the Time type
    '''
    time_type = Time("test_time")
    result, name = time_type()
    assert name == "test_time"
    assert isinstance(result, str)
    assert ":" in result

def test_timestamp_type():
    '''
        Test the Timestamp type
    '''
    timestamp_type = Timestamp("test_timestamp")
    result, name = timestamp_type()
    assert name == "test_timestamp"
    assert isinstance(result, int)

def test_timezone_type():
    '''
        Test the Timezone type
    '''
    timezone_type = TimeZone("test_timezone")
    result, name = timezone_type()
    assert name == "test_timezone"
    assert isinstance(result, str)

def test_day_of_week_type():
    '''
        Test the DayOfWeek type
    '''
    dow_type = DayOfWeek("test_dow")
    result, name = dow_type()
    assert name == "test_dow"
    assert result in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def test_uuid_type():
    '''
        Test the UUID type
    '''
    uuid_type = UUID("test_uuid")
    result, name = uuid_type()
    assert name == "test_uuid"
    assert isinstance(result, str)
    assert len(result) == 36  # UUID string length

def test_color_type():
    '''
        Test the Color type
    '''
    # Test different color formats
    color_types = ["name", "hex", "rgb"]
    for color_type in color_types:
        color = Color("test_color", color_type=color_type)
        result, name = color()
        assert name == "test_color"
        assert isinstance(result, str)

def test_job_title_type():
    '''
        Test the JobTitle type
    '''
    job = JobTitle("test_job")
    result, name = job()
    assert name == "test_job"
    assert isinstance(result, str)

def test_company_department_type():
    '''
        Test the CompanyDepartment type
    '''
    dept = CompanyDepartment("test_dept")
    result, name = dept()
    assert name == "test_dept"
    assert isinstance(result, str)

def test_file_extension_type():
    '''
        Test the FileExtension type
    '''
    ext = FileExtension("test_ext")
    result, name = ext()
    assert name == "test_ext"
    assert isinstance(result, str)

def test_social_media_handle_type():
    '''
        Test the SocialMediaHandle type
    '''
    platforms = ["twitter", "instagram", "facebook"]
    for platform in platforms:
        handle = SocialMediaHandle("test_handle", platform=platform)
        result, name = handle()
        assert name == "test_handle"
        assert isinstance(result, str)

def test_ip_address_type():
    '''
        Test the IPAddress type
    '''
    # Test IPv4
    ipv4 = IPAddress("test_ip", version="ipv4")
    result, name = ipv4()
    assert name == "test_ip"
    assert len(result.split(".")) == 4

    # Test IPv6
    ipv6 = IPAddress("test_ip", version="ipv6")
    result, name = ipv6()
    assert ":" in result

def test_latitude_longitude_type():
    '''
        Test the LatitudeLongitude type
    '''
    latlng = LatitudeLongitude("test_latlng")
    result, name = latlng()
    assert name == "test_latlng"
    assert isinstance(result, str)
    assert "," in result

def test_version_type():
    '''
        Test the Version type
    '''
    version = Version("test_version")
    result, name = version()
    assert name == "test_version"
    assert isinstance(result, str)
    assert len(result.split(".")) == 3

def test_url_type():
    '''
        Test the URL type
    '''
    url = URL("test_url")
    result, name = url()
    assert name == "test_url"
    assert isinstance(result, str)
    assert result.startswith(("http://", "https://"))

def test_sentence_type():
    '''
        Test the Sentence type
    '''
    sentence = Sentence("test_sentence")
    result, name = sentence()
    assert name == "test_sentence"
    assert isinstance(result, str)

def test_paragraph_type():
    '''
        Test the Paragraph type
    '''
    paragraph = Paragraph("test_paragraph")
    result, name = paragraph()
    assert name == "test_paragraph"
    assert isinstance(result, str)

def test_user_agent_type():
    '''
        Test the UserAgent type
    '''
    ua = UserAgent("test_ua")
    result, name = ua()
    assert name == "test_ua"
    assert isinstance(result, str)

def test_hash_type():
    '''
        Test the Hash type
    '''
    hash_types = ["md5", "sha1", "sha256"]
    for hash_type in hash_types:
        hash_gen = Hash("test_hash", hash_type=hash_type)
        result, name = hash_gen()
        assert name == "test_hash"
        assert isinstance(result, str)

def test_isbn_type():
    '''
        Test the ISBN type
    '''
    isbn = ISBN("test_isbn")
    result, name = isbn()
    assert name == "test_isbn"
    assert isinstance(result, str)

def test_isbn13_type():
    '''
        Test the ISBN13 type
    '''
    isbn13 = ISBN13("test_isbn13")
    result, name = isbn13()
    assert name == "test_isbn13"
    assert isinstance(result, str)

def test_ean_type():
    '''
        Test the EAN type
    '''
    ean = EAN("test_ean")
    result, name = ean()
    assert name == "test_ean"
    assert isinstance(result, str)

def test_sku_type():
    '''
        Test the SKU type
    '''
    sku = SKU("test_sku", prefix="TEST-", length=8)
    result, name = sku()
    assert name == "test_sku"
    assert result.startswith("TEST-")
    assert len(result) == len("TEST-") + 8

def test_mac_address_type():
    '''
        Test the MACAddress type
    '''
    mac = MACAddress("test_mac")
    result, name = mac()
    assert name == "test_mac"
    assert len(result.split(":")) == 6

def test_credit_card_number_type():
    '''
        Test the CreditCardNumber type
    '''
    card_types = ["visa", "mastercard", "amex", "discover"]
    for card_type in card_types:
        cc = CreditCardNumber("test_cc", card_type=card_type)
        result, name = cc()
        assert name == "test_cc"
        assert isinstance(result, str)

def test_iban_type():
    '''
        Test the IBAN type
    '''
    iban = IBAN("test_iban")
    result, name = iban()
    assert name == "test_iban"
    assert isinstance(result, str)

def test_bic_type():
    '''
        Test the BIC type
    '''
    bic = BIC("test_bic")
    result, name = bic()
    assert name == "test_bic"
    assert isinstance(result, str)

def test_probability():
    """Test that probability parameter works across different types"""
    test_types = [
        Text("test_text", value="fallback", probability=100),
        Number("test_number", value=5, probability=0),
        Bool("test_bool", probability=0),
        Email("test_email", probability=0),
        Date("test_date", probability=0)
    ]

    for test_type in test_types:
        result, name = test_type()
        if name == "test_text":
            assert result == "fallback"
        elif name == "test_number":
            assert result != 5
        else:
            assert result is None  # When probability is 0, should always get fallback value
