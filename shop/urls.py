from . import views #importing views.py which is in the same directory.
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="shopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="Search"),
    path('products/<int:myid>',views.productview,name="ProductView"),
    path('checkout/',views.checkout,name="Checkout")
]