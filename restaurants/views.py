from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[
            {
            "restaurant_name": "mashari",
            "food_type":"cake",
            },
            {
            "restaurant_name":"max",
            "food_type":"tea",
            },
            {
            "restaurant_name":"bigX",
            "food_type":"M&M",
            },
        ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":
            {
              "restaurant_name":"max",
              "food_type":"cake",
            }

    }
    return render(request, 'detail.html', context)
