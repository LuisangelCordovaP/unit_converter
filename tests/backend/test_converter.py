from backend.services.UnitConverter import UnitConverter
import pytest
from fastapi import HTTPException

class TestUnitConverter():

    @pytest.mark.parametrize("from_u, to_u, val, expected",
        [
        ("centimeter", "meter", 100, 1),
        ("kilometer", "meter", 2.5, 2500),
        ("inch", "mile", 5, 0.00007891414)
    ])
    def test_length_conversions(self, from_u, to_u, val, expected):
        converter = UnitConverter()
        result = converter.convert('length', from_u, to_u, val)
        assert result == pytest.approx(expected, rel=1e-6)

    
    @pytest.mark.parametrize("from_u, to_u, val, expected",
        [
            ('gram','pound', 750, 1.653467),
            ('ounce','milligram', 50, 1417476),
            ('kilogram', 'gram', 10, 10000)
        ])
    def test_weight_conversions(self, from_u, to_u, val, expected):
        converter = UnitConverter()
        result = converter.convert('weight', from_u, to_u, val)
        assert result == pytest.approx(expected, rel=1e-6)
        

    @pytest.mark.parametrize("from_u, to_u, val, expected",
        [
            ('celsius','fahrenheit', 100, 212),
            ('kelvin','celsius', 5, -268.15),
            ('fahrenheit', 'kelvin', 13.5, 262.8722)
        ])
    def test_temperature_conversions(self, from_u, to_u, val, expected):
        converter = UnitConverter()
        result = converter.convert('temperature', from_u, to_u, val)
        assert result == pytest.approx(expected, rel=1e-6)

    
    @pytest.mark.parametrize("category, from_u, to_u",
        [
            ("length", "centimeter", "invalid_unit"),
            ("temperature", "meter", "gram"),
            ("weight", "grams", "kelvin")
        ])
    def test_invalid_unit_param(self, category, from_u, to_u):
        converter = UnitConverter()
        with pytest.raises(HTTPException):
            converter.convert(category, from_u, to_u, 1)

    def test_invalid_category(self):
        converter = UnitConverter()
        with pytest.raises(HTTPException):
            converter.convert('invalid category', 'from_u', 'to_u', 1)
    
    @pytest.mark.parametrize(
            "category, from_u, to_u, value",
        [
            ('weight', 'pound', 'kilogram', -50),
            ('length', 'meter', 'millimeter', -101.1)
        ])
    def test_invalid_input_value(self, category, from_u, to_u, value):
        converter = UnitConverter()
        with pytest.raises(HTTPException):
            converter.convert(category, from_u, to_u, value)