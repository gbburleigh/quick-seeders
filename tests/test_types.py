import pytest
from seeder.types import *

def test_text_type():
    text = Text("test_column")
    result, name = text()
    assert name == "test_column"
    assert isinstance(result, str)

def test_number_type():
    number = Number("test_number")
    result, name = number()
    assert name == "test_number"
    assert isinstance(result, (int, float))

def test_email_type():
    email = Email("test_email")
    result, name = email()
    assert name == "test_email"
    assert "@" in result
    assert "." in result

def test_null_type():
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
    choices = ["A", "B", "C"]
    enum = Enum("test_enum", choices)
    result, name = enum()
    assert name == "test_enum"
    assert result in choices

def test_date_type():
    date = Date("test_date")
    result, name = date()
    assert name == "test_date"
    assert isinstance(result, str)
    # Could add more specific date format validation

def test_currency_type():
    currency = Currency("test_currency", symbol="$", min_value=10, max_value=20)
    result, name = currency()
    assert name == "test_currency"
    assert result.startswith("$")
    value = float(result.replace("$", ""))
    assert 10 <= value <= 20 