"""
URL configuration for djcms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('blog/admin/', admin.site.urls),

    path("blog/accounts/", include("accounts.urls")),
    path("blog/blogs/", include("blogs.urls")),
    path("blog/manage/", include("management.urls")),

    path("blog/", views.Index.as_view(), name="index"),
    path("blog/trendings/", views.Trendings.as_view(), name="trendings"),
    path("blog/latest/", views.Latest.as_view(), name="latest"),
    path("blog/popular/", views.Popular.as_view(), name="popular"),
    path("blog/search/", views.Search.as_view(), name="search"),
    path("blog/bookmark/", views.BookmarkView.as_view(), name="bookmark"),
    path("blog/terms-and-conditions/", views.TermsAndConditions.as_view(), name="terms_and_conditions"),
    path("blog/category/", views.CategoryView.as_view(), name="category"),
    path("blog/category/<slug:cat>/", views.GetCategory.as_view(), name="get_category"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
