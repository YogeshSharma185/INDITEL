
from django.urls import path
from . import myviews
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(myviews.index),name="ShopHome"),
    path('about/',login_required(myviews.about),name="about"),
    path('contact/',login_required(myviews.contact),name="contact"),
    # path('checkout499/',login_required(myviews.checkout499),name="checkout499"),
    # path('checkout599/',login_required(myviews.checkout599),name="checkout599"),
    # path('checkout699/',login_required(myviews.checkout699),name="checkout699"),
    # path('checkout799/',login_required(myviews.checkout799),name="checkout799"),
    # path('checkout999/',login_required(myviews.checkout999),name="checkout999"),
    # path('checkout3359/',login_required(myviews.checkout3359),name="checkout3359"),
    path('dthh/',login_required(myviews.dthh),name="dthh"),
    path('wifi/',login_required(myviews.wifii),name="wifi"),
    path('postpaidd/',login_required(myviews.postpaidd),name="postpaidd"),
    path('prepaidd/',login_required(myviews.prepaidd),name="prepaidd"),
    path('search/',login_required(myviews.unified_search),name="unified_search"),
       
    # payment
    path("pay/<int:amount>/", login_required(myviews.payment_form), name="initiate_payment"),
    path("pay/<int:amount>/create/", login_required(myviews.create_order), name="create_order"),
    path("payment-success/", login_required(myviews.payment_success), name="payment_success"),
    path("payment-failure/", login_required(myviews.payment_failure), name="payment_failure"),

    # path('signup/', login_required(myviews.signup, name='signup'),
    # path('login/', login_required(myviews.login, name='login'),
]    