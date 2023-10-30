from django.contrib import admin
from django.urls import path
from app.views import (
    near_hundred_view,
    string_splosion_view,
    cat_dog_view,
    lone_sum_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-1/near-hundred/<int:n>", near_hundred_view),
    path("warmup-2/string-splosion/<string>", string_splosion_view),
    path("string-2/cat-dog/<string>", cat_dog_view),
    path("logic-2/lone-sum/<int:a>/<int:b>/<int:c>", lone_sum_view),
]
