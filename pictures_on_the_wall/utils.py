from products.models import Product, Category, Hashtag, Artist

# My utilities

def special_filter(model, what):
    """" My helper function to filter the Products model 
    with the foreign keys to the 'model' to filter 'field' 
    by 'what' and return a QuerySet"""

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
    print(f"the filtered product QuerySet is {filtered_products}")
    return filtered_products

