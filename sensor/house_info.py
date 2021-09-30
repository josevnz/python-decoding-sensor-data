from datetime import date

ALL_RECORDS = 0


class HouseInfo:
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field: str, rec_area=0):
        field_data = []
        for record in self.data:
            if rec_area == ALL_RECORDS:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []

