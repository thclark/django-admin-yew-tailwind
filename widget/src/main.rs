mod app;

use app::Model;

fn main() {
    yew::Renderer::<Model>::new().render();
}
