import folium
import geocoder

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


def get_order_key_by_token(order_token: str) -> str:
    """Gets model .order_by key from a token given in path, if only token is not in excluded.
    Returns default_not_found value if token in excluded or not found."""
    default_not_found: str = ''
    excluded = {'order_by_teachers', }
    _storage = {
        'order_by_date': 'start_date',
        'order_by_city': 'city',
        'order_by_country': 'country',
        'order_by_teachers': 'teachers',
    }

    if order_token in excluded:
        return default_not_found
    return _storage.get(order_token, default_not_found)
