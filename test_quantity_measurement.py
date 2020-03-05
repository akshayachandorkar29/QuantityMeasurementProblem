import pytest
from quantity_measurement import QuantityMeasurement

qm = QuantityMeasurement()


def test_feet_given_zero_return_zero():
    result = qm.feet(0)
    assert result == 0


def test_feet_null_check():
    result = qm.feet("null")
    assert result == "null"


def test_feet_value_check():
    result = qm.feet(2)
    assert result == 2


def test_inch_value_check():
    result = qm.feet_to_inch(2)
    assert result == 24


def test_comparison_check_given_feet_zero_return_inch_zero():
    result = qm.feet_to_inch(0)
    assert result == 0


def test_comparing_length_one_feet_not_equal_to_one_inch():
    result = qm.feet_to_inch(1)
    assert result != 1


def test_comparing_length_one_inch_not_equal_to_one_feet():
    result = qm.inch_to_feet(1)
    assert result != 1


def test_comparing_length_one_feet_equal_to_twelve_inch():
    result = qm.feet_to_inch(1)
    assert result == 12

def test_comparing_length_twelve_inch_equal_to_one_feet():
    result = qm.inch_to_feet(12)
    assert result == 1


# Useacase 2 : comparing lengths 3 feet = 1 yard

def test_comparing_length_three_feet_equal_to_one_yard():
    result = qm.feet_to_yard(3)
    assert result == 1


def test_comparing_length_one_feet_not_equal_one_yard():
    result = qm.feet_to_yard(1)
    assert result != 1


def test_comparing_length_one_inch_not_equal_one_yard():
    result = qm.inch_to_yard(1)
    assert result != 1


def test_comparing_length_36_inch_equal_to_one_yard():
    result = qm.inch_to_yard(36)
    assert result == 1


def test_comparing_length_one_yard_equal_to_3_feet():
    result = qm.yard_to_feet(1)
    assert result == 3


def test_comparing_length_one_yard_equal_to_36_inch():
    feet = qm.yard_to_feet(1)
    result = qm.feet_to_inch(feet)
    assert result == 36


# USECASE-3 : comparing lengths 2 inch = 5 cm

def test_comparing_length_2_inch_equal_to_5_cm():
    result = qm.inch_to_centimeter(2)
    assert result == 5


# USECASE-4 : comparing 2inch+2inch=4inch

def test_adding_2_lengths_in_inches():
    result = qm.addition_of_two_lengths_inch_and_inch(2, 2)
    assert result == 4


def test_adding_2_lengths_in_feet():
    addition = qm.addition_of_two_lengths_inch_and_inch(1, 1)
    result = qm.feet_to_inch(addition)
    assert result == 24


def TestAdding2LengthsInFeetAndInch():
    result = qm.addition_of_two_lengths_feet_and_inch(1,2);
    assert result == 1


def TestAdding2LengthsInchAndCm():
    result = qm.addition_of_two_lengths_inch_and_cm(2,2.5);
    assert result == 3


# USECASE - 5 : comparing volumes in litre and gallon

def TestGallonToLitres():
    result = qm.gallon_to_litres(1.0)
    assert result == 3.78


def TestLitreToMl():
    result = qm.litre_to_ml(1)
    assert result == 1000


# USECASE-7 : comparing weights in grams

def TestKgToGram():
    result = qm.litre_to_ml(1)
    assert result == 1000


def TestTonneToKg():
    result = qm.litre_to_ml(1)
    assert result == 1000


# USECASE-8 : equating temperature in fahrenheit and celcius

def testFToC():
    result = qm.f_to_c(212)
    assert result == 100