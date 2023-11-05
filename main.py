### main.py
 
from taipy.gui import Gui
from pages.login import page
from pages.feed import frame
# from pages.map import map_md

 
pages = {
 
"home": page,
"feed": frame,
# "Map":map_md,

 
}
gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    gui_multi_pages.run(title="Clean Sight",
                        use_reloader=True,
                        port=5039)