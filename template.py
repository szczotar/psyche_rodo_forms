from datetime import datetime
from docxtpl import DocxTemplate
import jinja2

tpl = DocxTemplate('PATH/TO/THE/TEMPLATE/DOCUMENT')

YEAR = 2023  # this is just a dummy variable to showcase that variables can be used as well

context = {
    "today_date": datetime.now().strftime(format='%B %d, %Y'),
    "report_ref": "REP2023",
    "current_year": YEAR,
    "previous_year": YEAR-1,
    "current_year_total_sales": 150000,
    "previous_year_total_sales": 120000,
    "change_in_sales": "increase",
    "percentage_change": 25,
    "current_year_profit": 19500,
    "previous_year_profit": 10800,
    "footer_text": "Tags can be used in headers/footers as well.",
    }

jinja_env = jinja2.Environment(autoescape=True)
tpl.render(context, jinja_env)
tpl.save('PATH/TO/SAVE/THE/RESULTS/DOCUMENT')