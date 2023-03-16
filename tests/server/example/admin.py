from django.contrib import admin

from tests.server.example.models import ExampleModel


# class ExampleModelForm(ModelForm):
#     """A form that overrides the upload widget"""

#     class Meta:
#         model = ExampleStorageModel
#         widgets = {
#             "text": CloudFileWidget(
#                 bucket_identifier="gs://example-media-assets",
#                 path_prefix="direct_uploads/",
#             ),
#         }
#         fields = "__all__"


class ExampleModelAdmin(admin.ModelAdmin):
    """A basic admin panel"""

    # form = ExampleStorageModelForm

    # formfield_overrides = {
    #     DirectUploadFileField: {"widget": DirectUploadWidget(bucket_identifier="gs://example-media-assets")},
    # }


admin.site.register(ExampleModel, ExampleModelAdmin)
