import uuid


#Generator Slug
def get_product_slug(instance):
    return f"{instance.product_name}-{instance.price}-{str(uuid.NAMESPACE_URL).split('-')[0]}"
