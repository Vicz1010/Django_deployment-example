from django.conf.urls import url
from basicapp import views


# This is for template tagging for relative urls
app_name = 'basicapp'

urlpatterns = [
    # $ sign means for anything after relative or other
    url(r'relative/$',views.relative, name='relative'),
    url(r'other/$',views.other, name='other'),
]