"""
Property Tax Calculator 

A simple console application for calculating property tax based on property type and locality coefficient.

Demonstrates object-oriented programming in Python (inheritance, abstract classes, enums).
"""

import math
from abc import ABC, abstractmethod
from enum import Enum


class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


class EstateType(Enum):
    LAND = ("land", 0.85, "Agricultural land")
    BUILDING_SITE = ("building site", 9, "Building site")
    FOREST = ("forest", 0.35, "Forest")
    GARDEN = ("garden", 2, "Garden")

    def __init__(self, label, coef, description):
        self.label = label
        self.coef = coef
        self.description = description

    def __str__(self):
        return self.description        


class Property(ABC):
    def __init__(self, locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax(self):
        pass


class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        tax = self.area * self.estate_type.coef * self.locality.locality_coefficient
        return math.ceil(tax)
    
    def __str__(self):
        return (f"{self.estate_type.description}, locality {self.locality.name} "
               f"(coefficient {self.locality.locality_coefficient}), " 
               f"{self.area} m², tax {self.calculate_tax()} CZK")
   
   
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        
        if self.commercial:
            tax *= 2
        return math.ceil(tax)
    
    def __str__(self):
        if self.commercial:
            typ = "Commercial property"
        else:
            typ = "Resditential property"
        return (f"{typ}, locality {self.locality.name} " 
                f"(coefficient {self.locality.locality_coefficient}), " 
                f"{self.area} m², tax {self.calculate_tax()} CZK")


class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []

    def add_property(self, new_property):
        self.property_list.append(new_property)

    def calculate_tax(self):
        return sum(p.calculate_tax() for p in self.property_list)
         
    
    def __str__(self):
        text = f"Tax Report for {self.name}\n"
        text += "Properties:\n"

        for p in self.property_list:
            text += f" - {p}\n"
        text += "---------------------\n"
        text += f"\nTotal tax: {self.calculate_tax()} CZK"
        return text


# Testing section
if __name__ == "__main__":
    print("=== PROPERTY TAX ===")
    print("Enter type 'estate' (land) or 'residence' (house/apartment).")
    print("To finish, type 'exit'.\n")   

    name = input("Enter your name: ")
    report = TaxReport(name)

    while True:
        typ = input("Type of property (estate/residence, end = exit): ").lower()

        if typ == "exit":
            break

        if typ == "estate":
            area = int(input("Enter area: "))
            locality_name = input("Enter locality: ")
            coef = float(input("Enter locality coefficient: "))

            locality = Locality(locality_name, coef)

            print("Type of land (enter exactly): LAND, FOREST, GARDEN, BUILDING_SITE")
            
            try:
                estate_type = EstateType[input("Enter type: ").upper()]
            except KeyError:
                print("Invalid property type.")
                continue

            estate = Estate(locality, estate_type, area)
            report.add_property(estate)
            print("✔ Property added\n")

        elif typ == "residence":
            area = int(input("Enter area: "))
            locality_name = input("Enter locality: ")
            coef = float(input("Enter locality coefficient: "))
            commercial = input("Commercial? (yes/no) ").lower() == "yes"

            locality = Locality(locality_name, coef)

            residence = Residence(locality, area, commercial)
            report.add_property(residence)
            print("✔ Property added\n")
        else:
            print("Invalid property type.")

    print("\n=== TAX REPORT ===\n")
    print(report)     