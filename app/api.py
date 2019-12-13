# coding=utf8
from flask import Flask, jsonify
from app import utils, exceptions
import geocoder
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError, GeocoderUnavailable
import asyncio
import time

app = Flask(__name__)

geolocator = Nominatim()


@asyncio.coroutine
def transform(inputs):
    pairs = {}
    for input in inputs:
        if utils.is_location(input):
            try:
                coordinates = geolocator.geocode(input)
                pairs[input] = coordinates.latitude, coordinates.longitude
            except (GeocoderTimedOut, GeocoderServiceError, GeocoderUnavailable):
                time.sleep(5)
        elif utils.is_coordinates(input):
            try:
                location = geolocator.reverse(input)
                pairs[input] = location.address
            except (GeocoderTimedOut, GeocoderServiceError, GeocoderUnavailable):
                time.sleep(5)
    return pairs


@app.route('/')
def display():
    process = asyncio.run(transform(utils.mixed_inputs))
    message = 'converting map locations'
    if process:
        return jsonify(message, ("{process}".format(**vars())))
    else:
        raise exceptions.InvalidUsage(f"inputs were not valid addresses or coordinates",
                                      status_code=500)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
