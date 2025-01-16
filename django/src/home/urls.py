from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'home'


urlpatterns = [
    path('', views.views.HomeView.as_view(), name="home"),

    path('deside/', views.views.DesideView.as_view(), name="deside"),

    # path('watch/', views.views.WatchListView.as_view(), name="watch_list"),

    path("watch/<int:id>", views.views.watch_detail, name="watch_detail"),

    path("watch/<int:id>/update", views.views.record_update, name="record_update"),

    path("watch/<int:id>/delete", views.views.record_delete, name="record_delete"),

    path("record/",views.views.record,name="record"),

    path("record/edit/",views.views.record_edit,name="record_edit"),

    path("record/edit/detail/",views.views.record_edit_detail,name="record_edit_detail"),

    path("record/label/",views.views.record_label,name="record_label"),

    path("record/label<int:id>/update/",views.views.record_label_update,name="record_label_update"),

    path("record/label<int:label_title_code_id>",views.views.record_label_detail,name="record_label_detail"),

    path("record/label<int:id>/detail/update",views.views.record_label_detail_update,name="record_label_detail_update"),
]

