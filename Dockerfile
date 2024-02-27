# Create a base from a pre-compiled version of USD tools
# More info @ https://github.com/Plattar/python-usd
# Unlike the python-usd container, python-usd-ar also contains the Schema
# Definitions for ARKit and is useful for generating USDZ files with various
# AR Features.
# NOTE: As of 30/06/2022 this respository also builds and sets up 
# usdzconvert tools
# For more info on usdconvert, visit https://developer.apple.com/augmented-reality/tools/
FROM plattar/python-usd-ar:version-22.05b-slim-bullseye

COPY /usr/src/app/main.py main.py

CMD python main.py
