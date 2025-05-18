from fastapi import HTTPException


class UnitConverter:
    
    def convert(self, category: str, from_unit: str, to_unit: str, value: float):
        if category == 'length':
            result = LengthConverter().convert(value, from_unit, to_unit)
            return result
        
        elif category == 'weigth':
            result = WeightConverter().convert(value, from_unit, to_unit)
            return result
        
        elif category == 'temperature':
            result = TemperatureConverter().convert(value, from_unit, to_unit)
            return result

class LengthConverter:

    conversion_factors = {
        'meter' : 1,
        'kilometer' : 1000,
        'centimeter' : 0.01,
        'millimeter' : 0.001,
        'inch' : 0.0254,
        'foot' : 0.3048,
        'yard' : 0.9144,
        'mile' : 1609.344,
    }

    def convert(self, value, from_unit, to_unit):
        if not all(unit in self.conversion_factors for unit in (from_unit, to_unit)):
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Invalid unit for category 'length': '{from_unit}' or '{to_unit}' not recognized"
                    f"Allowed : {list(self.conversion_factors.keys())}"
                )
            )
        
        base_value = value * self.conversion_factors[from_unit]

        return base_value / self.conversion_factors[to_unit]

class WeightConverter:

    conversion_factors = {
        'gram': 1,
        'milligram': 0.001,
        'kilogram': 1000,
        'ounce': 28.34952,
        'pound': 453.5924, 
    }

    def convert(self,value, from_unit, to_unit):
        if not all(unit in self.conversion_factors for unit in (from_unit,to_unit)):
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Invalid unit for category 'weight': '{from_unit}' or '{to_unit}' not recognized"
                    f"Allowed : {list(self.conversion_factors.keys())}"
                )
            ) 
        base_value = value * self.conversion_factors[from_unit]
        return base_value / self.conversion_factors[to_unit]

class TemperatureConverter:
    conversion_factors = {
        'celsius': 1,
        'fahrenheit': -17.22222,
        'kelvin': -272.15,
    }

    def convert(self, value, from_unit, to_unit):
        if not all(unit in self.conversion_factors for unit in (from_unit, to_unit)):
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Invalid unit for category 'temperature': '{from_unit}' or '{to_unit}' not recognized"
                    f"Allowed : {list(self.conversion_factors.keys())}"
                )
            )
        base_value = value * self.conversion_factors[from_unit]
        return base_value / self.conversion_factors[to_unit]



    