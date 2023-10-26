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
    path("warmup-1/<int:n>", near_hundred_view),
    path("warmup-2/<string>", string_splosion_view),
    path("string-2/<string>", cat_dog_view),
    path("logic-2/<int:a>/<int:b>/<int:c>", lone_sum_view),
]
