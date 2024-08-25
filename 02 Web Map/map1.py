# import necessary libraries
import folium
import pandas

# Load the volcano data from a CSV file
data = pandas.read_csv("Volcanoes_USA.csv")

# Extract the latitude, longitude, and elevation data from the CSV file
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


# define a function to determine the color of a volcano based on its elevation
def color_producer(elevation):
    # If the elevation is less than 1000  meters, return green
    if elevation < 1000:
        return "green"
    # If the elevation is between 1000 and 3000 meters, return orange
    elif 1000 <= elevation <= 3000:
        return "orange"
    # If the elevation is greater than 3000 meters, return red
    else:
        return "red"


# Create a folium map with a starting location and zoom level
map = folium.Map(location=[40.75, -73.99], zoom_start=6, titles="Mapbox Bright")

# Create a feature group for the Volcanoes
fgv = folium.FeatureGroup("Volcanoes")

# Iterate over the latitude, longitude, and elevation data
for lt, ln, el in zip(lat, lon, elev):
    # Add a CircleMarker to the the feature group for each volcano
    fgv.add_child(
        folium.CircleMarker(
            # Set the location of the marker
            location=[lt, ln],
            # Set the popup text to display the elevation
            popup=str(el) + "m",
            # Set the fill color based on the elevation
            fill_color=color_producer(el),
            # Set border color to grey
            color="grey",
            # Set the opacity to 0.7 <- can be changed
            fill_opacity=0.7,
        )
    )

# Create a feature group for the population data
fgp = folium.FeatureGroup("Population")

# Add a GeoJson layer to the feature group
fgp.add_child(
    folium.GeoJson(
        # Load the GeoJson data from the file
        data=open("world.json", "r", encoding="utf-8-sig").read(),
        # Define a style function to determine the fill color based on population
        style_function=lambda x: {
            "fillColor": (
                "green"
                if x["properties"]["POP2005"] < 10000000
                else (
                    "orange"
                    if 10000000 <= x["properties"]["POP2005"] < 20000000
                    else "red"
                )
            )
        },
    )
)

# Add the feature groups to the map
map.add_child(fgv)
map.add_child(fgp)

# Add layer control to the map
map.add_child(folium.LayerControl())

# Save the map to an HTML file
map.save("my_map.html")

# Description:
# This code creates an interactive map using Folium that displays Volcanoes in the USA and their elevations
# The map also displays population data from a GeoJson file, with different colors indicating different population ranges.
# The volcanoes are represented by CircleMarkers, with their fill colors determined by their elevations.
# The map is saved to an HTML file called "my_map.html".

# Author: @vijaykumar.muppirisetti
# Date: 2024-08-25
# Version: 1.0
