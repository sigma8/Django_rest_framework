from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# Se necesita enlazar las vistas o views
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('snippets/', views.UserList.as_view()),
    path('snippets/<int:pk>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
