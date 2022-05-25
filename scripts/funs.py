#!/usr/bin/env python3

import logging

logging.basicConfig(
        format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO)

LOGGER = logging.getLogger(__file__)

def calc_bmi(height: int, weight: int)->float:
    """
    Calculate Body Mass Index
    :param height: Height in Feets and Inches
    :param weight: Weight in Pounds
    :return: bmi value
    """
    LOGGER.info("Calculating BMI")
    height_str = str(height)
    height = float((int(height_str[0])*30.48 + int(height_str[1:3])*2.54)/100)
    weight = float(weight*0.453)
    LOGGER.info("BMI calculation completed")
    return round(weight/(height*height),1)

def calc_quote(age: int, gender: str, bmi: float, discount: int)->int:
    """
    Find the quote based upon business rules
    :param age: Age of the person
    :param gender: Gender of the person
    :param discount: Discount
    :return: Quote
    """
    LOGGER.info("Calculating Quote")
    if 18<age<39 and (bmi<17.49 or bmi>38.5):
        LOGGER.info("Quote calculation completed")
        return 750 if gender=="Male" else 750 - (750*discount/100)
    elif 40<age<59 and (bmi<18.49 or bmi>38.5):
        LOGGER.info("Quote calculation completed")
        return 1000 if gender=="Male" else 1000 - (1000*discount/100)
    elif age>60 and (bmi<18.49 or bmi>45.5):
        LOGGER.info("Quote calculation completed")
        return 2000 if gender=="Male" else 2000 - (2000*discount/100)
    else:
        LOGGER.info("Quote calculation completed")
        return 500 if gender=="Male" else 500 - (500*discount/100)