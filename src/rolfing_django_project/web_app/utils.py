import folium
import geocoder

search_query = 'Санкт-Петербург, Розенштейна, 8-12'


def get_map_by_query(search_query: str, engine='osm') -> str:
    """Returns rendered html with map. Uses engine kwarg to navigate a target (default openstreetmap geocoding)."""

    search_query = str(search_query)
    try:
        location = getattr(geocoder, engine)(search_query)
        popup_html: str = search_query
        lat: float = location.current_result.north
        lng: float = location.current_result.east
        obj_map = folium.Map(location=[lat, lng], zoom_start=15)
        folium.Marker(location=[lat, lng],
                      tooltip=search_query,
                      popup=folium.Popup(popup_html)).add_to(obj_map)
        return obj_map._repr_html_()
    except AttributeError as e:
        print(e)
        return f'No valid map currently available for {search_query}.'
