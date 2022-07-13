from django.apps import apps


# Function to get NOM from Element
def get_nom_element(element, id):
    model = apps.get_model('product', str(element).capitalize())
    try:
        obj = model.objects.get(pk=id)
    except:
        obj = model.get_default_espece
    return obj.nom
