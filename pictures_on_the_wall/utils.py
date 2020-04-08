from products.models import Product, Category, Hashtag, Artist

# My utilities

def special_filter(model, field, what):
    """" My helper function to filter the Products model 
    with the foreign keys to the models to filter by 
    and return a QuerySet"""

    # the actual keyword argument for the filtering:
    filter_kwargs = model + '__' + field + '__' + 'iexact'
    # the actual filtering
    filtered_products = Product.objects.filter(**{filter_kwargs: what})
    
    return filtered_products

