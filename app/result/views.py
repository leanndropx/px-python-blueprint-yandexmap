from . import result
from flask import render_template, request
from app import functions

@result.route("/result")
def result():
    user_address = request.args.get("address")
    print(user_address)

    user_address_url = functions.search_address_on_map(user_address)


    user_coordinates_list = functions.get_array_user_coordinates(user_address_url)
    print(user_coordinates_list)


    lat_user = user_coordinates_list [0]
    long_user = user_coordinates_list [1]


    # this variable returns true or false
    address_inside_mkad = functions.verify_if_inside_mkad(lat_user,long_user)


    if address_inside_mkad:
        distance="Not necessary to calculate the distance because the address is inside MKAD"
    else:
        distance = functions.calculate_distance(lat_user,long_user)

    return render_template('result.html',user_address=user_address,distance=distance)

