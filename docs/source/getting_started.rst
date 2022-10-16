.. _getting_started:

===============
Getting Started
===============

.. TIP::
    A **complete example of a working server** is provided in `the tests folder of the source code <https://github.com/thclark/django-admin-yew-tailwind/tree/main/tests/server>`_.

.. _install_the_library

Install the library
===================

**library-name** is available on `pypi <https://pypi.org/>`_, so installation into your python virtual environment is dead
simple:

.. code-block:: py

    poetry add library-name

Not using poetry? It's highly opinionated, but it's your friend. Google it.


.. _install_the_django_app:

Install the django app
======================

Next, you'll need to install this as an app in your django settings:

.. code-block:: py

    INSTALLED_APPS = [
        # ...
        'library-name'
        # ...
    ]


.. _add_the_endpoints:

Add the endpoints
=================

Include the ``library-name`` URLS in your ``your_app/urls.py``:

.. code-block:: python

   from django.urls import include, re_path
   from library_name import urls as library_name_urls

   urlpatterns = [
      # ...other routes
      # Use whatever regex you want:
      re_path(r"^library-name/", include(library_name_urls))
   ]

Using ``python manage.py show_urls`` you can now see the endpoints appear in your app.
