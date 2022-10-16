# django-admin-yew-tailwind

To be completed... I'm currently messing around using Rust with Yew and Tailwind, to build django admin widgets.

There are no guarantees I'll ever maintain this beyond this lazy Sunday morning. Use completely at your own risk.

## The goal

- A solution where I can build powerful widgets for Django Admin, so that I can build widgets in a way akin to how I'd build a React app (i.e. not building raw HTML, js and css),

- where I don't have to spend the next five hundred thousand years trying to configure parcel or rollup or whatever,

- and where, when there's possibility of multiple widgets from differnet providers/apps on the page, there is minimal/no risk of conflicts between JS libs.
  - \*For example, hooking two diffeerent instances of React into the DOM spells utter disaster, same goes for lots of JS libraries especially where any kind of state management is concerned

## Inspired by:

This Medium tutorial:

https://dev.to/arctic_hen7/how-to-set-up-tailwind-css-with-yew-and-trunk-il9

And by this introduction to Yew:

https://yew.rs/docs/concepts/components/introduction
