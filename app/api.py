from flask import Flask, request, jsonify, url_for
from app import utils, exceptions
import geocoder
from geopy.geocoders import Nominatim
import asyncio
import time

app = Flask(__name__)

geolocator = Nominatim()


@asyncio.coroutine
def transform(inputs):
    pairs = {}
    for input in inputs:
        if utils.is_location(input):
            coordinates = geolocator.geocode(input)
            pairs[input] = coordinates.latitude, coordinates.longitude
        elif utils.is_coordinates(input):
            location = geolocator.reverse(input)
            pairs[input] = location.address
            time.sleep(5)
    return pairs


@asyncio.coroutine
def introduce():
    message = {
        'Requesting': 'location formats conversion...',
    }
    return jsonify(message)


@app.route('/')
def display():
    process = asyncio.run(transform(utils.mixed_inputs))
    message = 'converting map locations'
    if process:
        return jsonify(message, ("{process}".format(**vars())))
    else:
        raise exceptions.InvalidUsage(f"Something went wrong, please input a valid address or coordinates value",
                                      status_code=500)

    # asyncio.set_event_loop(loop)
    # # loop.run_until_complete(asyncio.gather(*task))
    # tasks = [
    #          asyncio.ensure_future(transform(utils.mixed_inputs))]

    # try:
    # process
    # operation = loop.run_until_complete(asyncio.wait(tasks))
    # finally:
    # loop.close()


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
