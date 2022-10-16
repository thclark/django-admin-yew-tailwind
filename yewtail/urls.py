from django.urls import path

from yewtail.events.views import GoogleCloudEventsView
from yewtail.tasks.views import GoogleCloudSubscriberTaskView, GoogleCloudTaskView


urlpatterns = [
    path(r"tasks/<task_name>", GoogleCloudTaskView.as_view(), name="gcp-tasks"),
    path(r"subscriber-tasks/<task_name>", GoogleCloudSubscriberTaskView.as_view(), name="gcp-subscriber-tasks"),
    path(r"events/<event_kind>/<event_reference>", GoogleCloudEventsView.as_view(), name="gcp-events"),
]
