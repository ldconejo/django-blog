from django.urls import path
from polling.views import PollListView, DetailListView

urlpatterns = [
    path('', PollListView.as_view(), name="poll_index"),
    path('polls/<int:pk>/', DetailListView.as_view(), name="poll_detail")
]