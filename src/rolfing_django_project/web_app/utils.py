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
