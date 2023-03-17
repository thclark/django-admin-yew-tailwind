from django.contrib import admin

from .models import YewtailModel


# class YewtailModelForm(ModelForm):
#     """A form that overrides the upload widget"""

#     class Meta:
#         model = YewtailModel
#         widgets = {
#             "text": CloudFileWidget(
#                 bucket_identifier="gs://example-media-assets",
#                 path_prefix="direct_uploads/",
#             ),
#         }
#         fields = "__all__"


class YewtailModelAdmin(admin.ModelAdmin):
    """A basic admin panel"""

    # form = YewtailModelModelForm

    # formfield_overrides = {
    #     DirectUploadFileField: {"widget": DirectUploadWidget(bucket_identifier="gs://example-media-assets")},
    # }


admin.site.register(YewtailModel, YewtailModelAdmin)
