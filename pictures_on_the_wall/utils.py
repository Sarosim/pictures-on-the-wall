from products.models import Product, Category, Hashtag, Artist, Rating

# My utilities

def special_filter(model, what):
    """ My helper function to filter the Products model \n
    with the foreign keys to the 'model' to filter by 'what' \n
    model - The name of the linked model in the products app \n
    what - The instance we are looking for."""

    # constructing 'field' for the kwargs
    # we use the 'model'+'_name' fields from the models
    field = model + '_name'

    # the actual keyword argument for the filtering:
    filter_kwargs = model + '__' + field + '__' + 'iexact'
    # the actual filtering
    filtered_products = Product.objects.filter(**{filter_kwargs: what})
    return filtered_products

def get_the_ratings_for(product):
    """ Utility function calculating average rating, rating percentage and a\n
    counter for the ratings for a given product and returns it in a dictionary"""
    ratings = Rating.objects.filter(product=product)
    ratings_total = 0
    ratings_count = 0
    if ratings:
        for rating in ratings:
            ratings_total += rating.rating
            ratings_count += 1
        ratings_average = ratings_total / ratings_count
    else:
        ratings_average = 0
    ratings_percent = round(ratings_average * 20)
    ratings_data = {
        "ratings_average": ratings_average,
        "ratings_percent": ratings_percent,
        "ratings_count": ratings_count
    }
    return ratings_data