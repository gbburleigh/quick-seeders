# Seeder Package

This package contains the core functionality for generating seed data.

## Structure

### seed.py

The main seeder implementation containing the `Seeder` class. This class handles:

- Converting schema definitions to generators
- Generating seed data
- Exporting data to different formats (JSON, CSV, SQL)
- Managing the export directory

Key components:
- `Seeder.seed()`: Generates data based on schema or generators
- `Seeder.to_json()`: Exports data to JSON format
- `Seeder.to_csv()`: Exports data to CSV format
- `Seeder.to_sql()`: Exports data to SQL insert statements

### types.py

Contains all the data type generators. Each type is implemented as a class with:

- `__init__`: Configures the generator with name and options
- `__call__`: Generates a single value
- `__repr__`: String representation for debugging

Common features across types:
- `name`: Column name for the generated data
- `probability`: Chance of generating a value vs null (0-100)
- `handle_probability()`: Common probability handling logic

#### Date/Time Types

Special handling for date and time types:
- Multiple input formats (ISO, date-only, keywords)
- Relative time specifications (`+1d`, `-2h`, etc.)
- Flexible range definitions
- Timezone awareness

#### Value Types

Types that generate specific value formats:
- Basic values (text, numbers, booleans)
- Formatted strings (emails, phones, URLs)
- Geographic data
- Financial information
- Business data

#### Null Handling

All types support probability-based null values:
- 100 = never null
- 0 = always null
- 1-99 = percentage chance of value vs null

## Usage

See the main README.md for usage examples and the complete list of available types. 