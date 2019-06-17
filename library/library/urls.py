
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path('borrower/', include('borrower.urls')),
    path('book_loan/', include('book_loan.urls')),
    path('fine/', include('fine.urls')),
    path('book_search/', include('book_search.urls')),
    path('book_return/', include('book_return.urls')),
    path('', include('home.urls')),

]
