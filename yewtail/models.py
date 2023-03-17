from django.db.models import Model, TextField


class YewtailModel(Model):
    """
    An example model that will use the widget in its admin.
    You'll need to make the migrations for the test app:
    ```
       python manage.py makemigrations yewtail
    ```
    """

    text = TextField(max_length=32)
