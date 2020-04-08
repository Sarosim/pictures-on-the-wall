from products.models import Product, Category, Hashtag, Artist

# My utilities

def special_filter(model, what):
    """" My helper function to filter the Products model \n
    with the foreign keys to the 'model' to filter by 'what' \n
    model - The name of the linked model in the products app \n
    what - The instance we are looking for."""

    # constructing 'field' for the kwargs
    if model == 'hashtag':
        # the hashtag model doesn't have a hashtag_name field
        field = 'hashtag'
    else:
        # we use the 'model'+'_name' fields from the other models
        field = model + '_name'

    # the actual keyword argument for the filtering:
    filter_kwargs = model + '__' + field + '__' + 'iexact'
    # the actual filtering
    filtered_products = Product.objects.filter(**{filter_kwargs: what})
    return filtered_products

