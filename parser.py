import cianparser

import cianparser

moscow_parser = cianparser.CianParser(location="Химки")
data = moscow_parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1000}, with_extra_data=True)



# moscow_parser = cianparser.CianParser(location="Жуковский")
# data = moscow_parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1000})


