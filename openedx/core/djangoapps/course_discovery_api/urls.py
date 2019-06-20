"""
course_discovery  API URLs.
"""

from django.conf import settings
from django.conf.urls import include, url

from openedx.core.djangoapps.course_discovery_api import views

urlpatterns = [
    url(
        r'^api/v1/course/search/discovery/$',views.CourseSearchView.as_view(), name='course_search_detail'
    ),
    url(
        r'^api/v1/course/search/enrollment/$',views.CourseSearchEnrollmentView.as_view(), name='course_search_enrollment_detail'
    ),
    url(
        r'^api/v1/course/category/$',views.CourseCategoryView.as_view(), name='course_category_detail'
    ),
  ]

