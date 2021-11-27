import datetime


# Needed for SQL BETWEEN
class DateConverter:
    def convert(dates):
        # If there is no value for them
        if not dates:
            from_date = to_date = None

        from_date = dates['start_date'] if 'start_date' in dates else datetime.date(2021, 1,
                                                                                    1)  # near value to the project beginning
        to_date = dates['end_date'] if 'end_date' in dates else datetime.date.today()

        return from_date, to_date
