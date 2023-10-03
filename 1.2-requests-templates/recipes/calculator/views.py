from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

context = {}


def get_recipe(request, dish):
    context['recipe'] = DATA[dish]
    servings = request.GET.get('servings')
    if servings:
        index = int(servings)
        new_dict = {}
        new_dict.update(
            (key, value * index) for key, value in context['recipe'].items()
        )
        context['recipe'] = new_dict
        return context
    else:
        return context


def omlet_view(request):
    get_recipe(request, 'omlet')
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    get_recipe(request, 'pasta')
    return render(request, 'calculator/index.html', context)


def buter_view(request):
    get_recipe(request, 'buter')
    return render(request, 'calculator/index.html', context)
