use yew::prelude::*;

pub enum Msg {
    AddOne,
}

pub struct Model {
    value: i64,
}

impl Component for Model {
    type Message = Msg;
    type Properties = ();

    fn create(_ctx: &Context<Self>) -> Self {
        Self {
            value: 3,
        }
    }

    fn update(&mut self, _ctx: &Context<Self>, msg: Self::Message) -> bool {
        match msg {
            Msg::AddOne => {
                self.value += 1;
                // the value has changed so we need to
                // re-render for it to appear on the page
                true
            }
        }
    }

    fn view(&self, ctx: &Context<Self>) -> Html {
        // This gives us a component's "`Scope`" which allows us to send messages, etc to the component.
        let link = ctx.link();
        html! {
            <div>
                <button class={classes!("bg-teal-500")} onclick={link.callback(|_| Msg::AddOne)}>{ "+1" }</button>
                <p>{ self.value }</p>
                <p class={classes!("bg-red-100")}>{"Test!"}</p>
            </div>
        }
    }
}
