import random
from typing import Any, Dict, List, Union
from datetime import datetime
from faker import Faker

fake = Faker("en_US")

def handle_probability(value, fallback, probability):
    sample = random.random()
    if sample < probability / 100:
        return value
    else:
        return fallback

'''
    @param name: The name of the column
    @param value: The possible fallback value if the column is not null. Can be another faked data type
    @param probability: The probability of the column being null
'''
class Null:
    def __init__(self, name, value=None, probability=100):
        self.name = name
        self.value = value
        self.probability = probability

    def __call__(self, *args, **kwargs):
        if callable(self.value):
            value = self.value()[0]
        else:
            value = self.value
        return (handle_probability(value, None, self.probability), self.name)
        
    def __str__(self):
        return str(self.value)
        
    def __repr__(self):
        return "Null()"


'''
    @param name: The name of the column
    @param value: The int value to be used. If not provided, a random int will be generated.
'''
class Int:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __call__(self, *args, **kwargs):
        if callable(self.value):
            value = self.value()[0]
        else:
            value = self.value
        return (value if value else random.randint(1, 99999999), self.name)
        
    def __str__(self):
        return str(self.value)
        
    def __repr__(self):
        return "Int()"

'''
    @param name: The name of the column
    @param value: The float or int value to be used. If not provided, a random int will be generated.
'''
class Number:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __call__(self, *args, **kwargs):
        if callable(self.value):
            value = self.value()[0]
        else:
            value = self.value
        return (value if value else random.randint(1, 99999999), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Number()"

'''
    @param name: The name of the column
    @param value: The bool value to be used. If not provided, a random bool will be generated.
'''
class Bool:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __call__(self, *args, **kwargs):
        if callable(self.value):
            value = self.value()[0]
        else:
            value = self.value
        return (value if value else random.choice([True, False]), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Bool()"

'''
    @param name: The name of the column
    @param value: The str value to be used. If not provided, an empty str will be generated.
    @param probability: The probability of the text being empty. Defaults to 0
'''
class Text:
    def __init__(self, name, value=None, probability=0):
        self.name = name
        self.value = value
        self.probability = probability

    def __call__(self, *args, **kwargs):
        if callable(self.value):
            value = self.value()[0]
        else:
            value = self.value
        return (value if value else handle_probability(value, fake.sentence(nb_words=10), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Text()"

'''
    @param name: The name of the column
    @param value: The date value to be used. If not provided, the current date will be generated.
    @param probability: The probability of the date being today. Defaults to 0
'''
class Date:
    def __init__(self, name, value=None, probability=0):
        self.name = name
        self.value = value
        self.probability = probability

    def __call__(self, *args, **kwargs):
        if callable(self.value):
            value = self.value()[0]
        else:
            value = self.value
        return (value if value else handle_probability(value, str(datetime.now()), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Date()"

'''
    @param name: The name of the column
    @param symbol: The symbol of the currency. Defaults to $
    @param min_value: The minimum value of the currency. Defaults to 0
    @param max_value: The maximum value of the currency. Defaults to 1000
    @param probability: The probability of the currency being null. Defaults to 100
'''
class Currency:
    def __init__(self, name, symbol="$", min_value=0, max_value=1000, probability=0):
        self.name = name
        self.symbol = symbol
        self.min_value = min_value
        self.max_value = max_value
        self.probability = probability

    def __call__(self, *args, **kwargs):
        value = f"{self.symbol}{random.randint(self.min_value, self.max_value):.2f}"
        return (handle_probability(None, value, self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Currency()"

'''
    @param name: The name of the column
    @param choices: The list of choices to be used. If not provided, an empty list will be generated.
    @param probability: The probability of the enum being null. Defaults to 0
'''
class Enum:
    def __init__(self, name, choices: List[Any], probability=0):
        if not choices:
            raise ValueError("Enum must have at least one choice.")
        self.name = name
        self.choices = choices
        self.probability = probability

    def __call__(self, *args, **kwargs):
        choices = [(choice() if callable(choice) else choice) for choice in self.choices]
        return (handle_probability(None, random.choice(choices), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Enum()"

'''
    @param name: The name of the column
    @param prefix: The prefix of the id. Defaults to an empty str
    @param probability: The probability of the id being null. Defaults to 0
'''
class ID:
    def __init__(self, name, prefix="", probability=0):
        self.name = name
        self.prefix = prefix
        self.probability = probability

    def __call__(self, *args, **kwargs):
        uuid = fake.uuid4()
        if len(self.prefix) > len(uuid):
            raise ValueError('Prefix cannot be longer than the id')
        id_value = self.prefix + uuid[len(self.prefix):]
        return (handle_probability(None, id_value, self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "ID()"

'''
    @param name: The name of the column
    @param probability: The probability of the name being null. Defaults to 0
'''
class Name:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.name(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Name()"

'''
    @param name: The name of the column
    @param probability: The probability of the address being null. Defaults to 0
'''
class Address:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.address(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Address()"

'''
    @param name: The name of the column
    @param email_type: The type of the email. Defaults to random
    @param domain: The domain of the email. Defaults to None
    @param probability: The probability of the email being null. Defaults to 0
'''
class Email:
    def __init__(self, name, email_type="random", domain=None, probability=0):
        self.name = name
        self.email_type = email_type.lower()
        self.domain = domain
        self.probability = probability
        if self.email_type not in ("random", "safe", "free", "company", "specific"):
            raise ValueError("Invalid email type. Must be one of: random, safe, free, company, specific")
        if self.email_type == "specific" and self.domain is None:
            raise ValueError("Domain must be specified when email_type is 'specific'")

    def __call__(self, *args, **kwargs):
        if self.email_type == "random":
            email = fake.email()
        elif self.email_type == "safe":
            email = fake.safe_email()
        elif self.email_type == "free":
            email = fake.free_email()
        elif self.email_type == "company":
            email = fake.company_email()
        else:  # specific
            email = fake.email(domain=self.domain)
        return (handle_probability(None, email, self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Email()"

'''
    @param name: The name of the column
    @param probability: The probability of the phone being null. Defaults to 0
    @param locale: The locale of the phone. Defaults to None
'''
class Phone:
    def __init__(self, name, probability=0, locale=None):
        self.name = name
        self.probability = probability
        self.locale = locale
        if self.locale:
            try:
                Faker(self.locale)
            except AttributeError:
                raise ValueError(f"Invalid locale: {self.locale}")

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.phone_number(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Phone()"

'''
    @param name: The name of the column
    @param probability: The probability of the website being null. Defaults to 0
'''
class Website:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.url(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Website()"

'''
    @param name: The name of the column
    @param probability: The probability of the domain name being null. Defaults to 0
'''
class DomainName:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.domain_name(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "DomainName()"

'''
    @param name: The name of the column
    @param probability: The probability of the domain word being null. Defaults to 0
'''
class DomainWord:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.domain_word(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "DomainWord()"

'''
    @param name: The name of the column
    @param probability: The probability of the TLD being null. Defaults to 0
'''
class TLD:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.tld(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "TLD()"

'''
    @param name: The name of the column
    @param probability: The probability of the country being null. Defaults to 0
'''
class Country:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.country(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Country()"

'''
    @param name: The name of the column
    @param probability: The probability of the state being null. Defaults to 0
    @param state_abbr: Whether to return state abbreviation instead of full name. Defaults to False
'''
class State:
    def __init__(self, name, probability=0, state_abbr=False):
        self.name = name
        self.probability = probability
        self.state_abbr = state_abbr

    def __call__(self, *args, **kwargs):
        state = fake.state_abbr() if self.state_abbr else fake.state()
        return (handle_probability(None, state, self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "State()"

'''
    @param name: The name of the column
    @param probability: The probability of the city being null. Defaults to 0
'''
class City:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.city(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "City()"

'''
    @param name: The name of the column
    @param probability: The probability of the zip code being null. Defaults to 0
'''
class Zip:
    def __init__(self, name, probability=0):
        self.name = name
        self.probability = probability

    def __call__(self, *args, **kwargs):
        return (handle_probability(None, fake.postcode(), self.probability), self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Zip()"