### main.py
 
from taipy.gui import Gui
from pages.login import page
from pages.feed import frame
 
pages = {
 
"home": page,
"feed": frame,
 
}
 
Gui(pages=pages).run(dark_mode=True)