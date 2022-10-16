from django.db.models import Model, TextField


class ExampleModel(Model):
    """
    An example model that will use the widget in its admin.
    You'll need to make the migrations for the test app:
    ```
       python manage.py makemigrations example
    ```
    """

    text = TextField(max_length=32)

    # class Meta:
    #     app_label = "tests"
