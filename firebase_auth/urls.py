from . import views

urlpatterns = [
    path('reset/',views.reset),
    path('postReset/', views.postReset),
]
