# Property Tax Calculator (OOP in Python)
## About the project

This project is a simple console application for calculating property tax based on different property types and locality coefficients.

The goal of this project was to practice object-oriented programming (OOP) concepts in Python, including inheritance, abstraction, and working with enums. 

## Features

- Calculation of property tax for: 

    - Land (different types: garden, forest, building site, etc.)
    - Residentail properties
    - Commercial properties
- Use of locality coefficients
- Support for multiple properties in one tax report
- Console interface for user input
- Automatic calculation of total tax 

## Project Structure

The project is built using OOP principles:

- **Abstract class** `Property` - defines a common interface
- **Classes:**
    - `Estate` - for land properties
    - `Residence` - for houses/apartments
- **Enum `EstateType`** - defines types of land with coefficients
- **Class `Locality`** - stores location and coefficient
- **Class `TaxReport`** - aggregates properties and calculates total tax

## What I Learned

- Object-oriented programming in Python

- Working with abstract classes (`ABC`)
- Using `Enum` for cleaner and safer code
- Designing class structure and relationships
- Handling user input in console applications
- Structuring a larger Python script

## How to Run

1. Clone the repository:

```
bash 
git clone https://github.com/your-username/property-tax-calculator.git
```

2. Navigate to the project folder:
```
bash
cd property-tax-calculator
```

3. Run the script: 
```
bash
python property_tax_calculator.py
```

4. Follow the instructions in the console: 
- Choose property type (estate or residence)
- Enter required values
- View the calculated tax report

### Alternative
You can also download the project as a ZIP file, extract it, and run the script locally.

## Example Output

```
=== TAX REPORT ===

Tax Report for Kristyna
Properties:
    - Garden, locality Brno (coefficient 3.0), 500 m², tax 3000 CZK
    - Commercial property, locality Praha (coefficient 4.0), 100 m², tax 12000 CZK
---------------------

Total tax: 15000 CZK
```

## Future Improvements

- Add input validation (better error handling)

- Separate logic and user interface
- Convert to a sipmle web app or API
- Add unit tests

## Author

Kristyna Slamova
- [LinkedIn](https://linkedin.com/in/kristýna-slámová-3a6905168)
- [GitHub](https://github.com/slamova-labs)