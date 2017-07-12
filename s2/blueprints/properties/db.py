"""db related helper functions."""


def create_filter(query):
    """Create a mongo filter to use with find."""
    mongo_filter = {}

    if query.getlist('Location') and query.getlist('Location') != ['']:
        mongo_filter.update(
            {'Location': {'$in': query.getlist('Location')}}
        )
    if query.get('minPrice'):
        mongo_filter.update(
            {'Price': {'$gte': int(query.get('minPrice'))}}
        )
    if query.get('maxPrice'):
        price_dict = mongo_filter.get('Price')
        price_dict.update({'$lte': int(query.get('maxPrice'))})
        mongo_filter.update(
            {'Price': price_dict}
        )
    if query.get('minSquareMeters'):
        mongo_filter.update(
            {'Square Meters': {'$gte': int(query.get('minSquareMeters'))}}
        )
    if query.get('maxSquareMeters'):
        sq_dict = mongo_filter.get('Square Meters')
        sq_dict.update({'$lte': int(query.get('maxSquareMeters'))})
        mongo_filter.update(
            {'Square Meters': sq_dict}
        )
    if query.get('Availability') in ['Sale', 'Rent']:
        mongo_filter.update(
            {'Availability': query.get('Availability')}
        )
    if query.getlist('Type') and query.getlist('Type') != ['']:
        mongo_filter.update(
            {'Type': {'$in': query.getlist('Type')}}
        )

    return mongo_filter
