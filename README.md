# django-admin-yew-tailwind

To be completed... I'm currently messing around using Rust with Yew and Tailwind, to build django admin widgets.

There are no guarantees I'll ever maintain this beyond this lazy Sunday morning. Use completely at your own risk.

Update: it's a Friday morning now. I'm upping my game a fraction with this... still use completely at your own risk.

## The goal

- A solution where I can build powerful widgets for Django Admin, so that I can build widgets in a way akin to how I'd build a React app (i.e. not building raw HTML, js and css),

- where I don't have to spend the next five hundred thousand years trying to configure parcel or rollup or whatever,

- and where, when there's possibility of multiple widgets from differnet providers/apps on the page, there is minimal/no risk of conflicts between JS libs.
  - \*For example, hooking two different instances of React into the DOM spells utter disaster, same goes for lots of JS libraries especially where any kind of state management is concerned

## Inspired by:

This Medium tutorial:

https://dev.to/arctic_hen7/how-to-set-up-tailwind-css-with-yew-and-trunk-il9

And by this introduction to Yew:

https://yew.rs/docs/concepts/components/introduction

## The general approach

I'm going to:

- Build a tiny little app in Yew, which constitutes the widget which will get shown in the admin
- The `<body>` will contain the widget html only. The `<head>` will contain assets for the widget only.
- I'll use `trunk serve` to build the HTML continuously, which:
  - Has the limitation that it has to work on a valid top level index.html file,
  - And therefore can't be used to render html directly into a django template. So,
  - I'll use a trunk pipeline to execute a short python script that extracts `index.html` out to `head.html` and `body.html`
  - And write a separate widget template on the side of the django lib to include these files,
  - So when django renders the widget it gets the built HTML from yew/trunk.
- Obviously, the widget won't be able to make much (any) use of template variables.
  - This can still receive django-rendered data by templating json data into a DOM node. That has the advantage of being able to be tested on the purely yew-side by putting test data into the DOM node in the widget's raw `index.html`.

## Get started

Assuming you're in a fresh new devcontainer (which has a postgres container attached)

### Developing the widget

```
cd widget
trunk serve
```

### Developing yewtail (the django lib that uses the widget)

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

You should then go to [the admin page](http://localhost:8000/admin/), click add and see the widget
