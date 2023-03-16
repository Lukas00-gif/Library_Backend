from back.views import LibraryListAndCreate, LibraryEditAndDelete

from django.urls import path

urlpatterns = [
    path('',LibraryListAndCreate.as_view()),
    path('<int:pk>', LibraryEditAndDelete.as_view())
]
