from utils.for_str import string_handle


def market_table(table_td, company_type_td):
    # all_table_body[1].find_all('td')
    if company_type_td == False:
        last_trading_price = string_handle(table_td[0].text)
        closing_price = string_handle(table_td[1].text)
        last_update = string_handle(table_td[2].text)
        days_range = string_handle(table_td[3].text)
        change_prev = string_handle(table_td[4].text)
        change_next = string_handle(table_td[6].text)
        days_value = string_handle(table_td[5].text)
        fiftytwo_weeks_moving_range = string_handle(table_td[7].text)
        opening_price = string_handle(table_td[8].text)
        days_volume = string_handle(table_td[9].text)
        adjusted_opening_price = string_handle(table_td[10].text)
        days_trade = string_handle(table_td[11].text)
        yesterday_closing_price = string_handle(table_td[12].text)
        market_capitalization = string_handle(table_td[13].text)

        return {"last_trading_price": last_trading_price,
                "last_trading_yield": "N/A",
                "closing_price": closing_price,
                "last_update": last_update,
                "days_range": days_range,
                "change_prev": change_prev,
                "change_next": change_next,
                "days_value": days_value,
                "fiftytwo_weeks_moving_range": fiftytwo_weeks_moving_range,
                "opening_price": opening_price,
                "days_volume": days_volume,
                "adjusted_opening_price": adjusted_opening_price,
                "days_trade": days_trade,
                "yesterday_closing_price": yesterday_closing_price,
                "market_capitalization": market_capitalization,
                "remaining_maturity": "N/A"
                }
    else:
        last_trading_price = string_handle(table_td[0].text)
        last_trading_yield = string_handle(table_td[2].text)
        closing_price = string_handle(table_td[1].text)
        last_update = string_handle(table_td[4].text)
        days_range = string_handle(table_td[3].text)
        change_prev = string_handle(table_td[6].text)
        change_next = string_handle(table_td[8].text)
        days_value = string_handle(table_td[5].text)
        fiftytwo_weeks_moving_range = string_handle(table_td[7].text)
        opening_price = string_handle(table_td[10].text)
        days_volume = string_handle(table_td[9].text)
        adjusted_opening_price = string_handle(table_td[12].text)
        days_trade = string_handle(table_td[11].text)
        yesterday_closing_price = string_handle(table_td[14].text)
        market_capitalization = string_handle(table_td[13].text)
        remaining_maturity = string_handle(table_td[15].text)

        return {
            "last_trading_price": last_trading_price,
            "last_trading_yield": last_trading_yield,
            "closing_price": closing_price,
            "last_update": last_update,
            "days_range": days_range,
            "change_prev": change_prev,
            "change_next": change_next,
            "days_value": days_value,
            "fiftytwo_weeks_moving_range": fiftytwo_weeks_moving_range,
            "opening_price": opening_price,
            "days_volume": days_volume,
            "adjusted_opening_price": adjusted_opening_price,
            "days_trade": days_trade,
            "yesterday_closing_price": yesterday_closing_price,
            "market_capitalization": market_capitalization,
            "remaining_maturity": remaining_maturity
        }


def basic_table(table_td, company_type_td):
    if company_type_td == False:
        authorized_capital = string_handle(table_td[0].text)
        debut_trading_date = string_handle(table_td[1].text)
        paid_up_capital = string_handle(table_td[2].text)
        type_of_instrument = string_handle(table_td[3].text)
        face_par_value = string_handle(table_td[4].text)
        market_lot = string_handle(table_td[5].text)
        total_outstanding_security = string_handle(table_td[6].text)
        sector = string_handle(table_td[7].text)

        return {
            "issuer": "N/A",
            "tenure": "N/A",
            "issue_date": "N/A",
            "cupon_rate": "N/A",
            "debut_trading_date_basic": "N/A",
            "cupon_frequency": "N/A",
            "maturity_date": "N/A",
            "security_catagory": "N/A",
            "electronic_share_basic": "N/A",
            "year_basis": "N/A",
            "authorized_capital": authorized_capital,
            "debut_trading_date": debut_trading_date,
            "paid_up_capital": paid_up_capital,
            "type_of_instrument": type_of_instrument,
            "face_par_value": face_par_value,
            "market_lot": market_lot,
            "total_outstanding_security": total_outstanding_security,
            "sector": sector
        }

    else:
        issuer = string_handle(table_td[0].text)
        tenure = string_handle(table_td[6].text)
        issue_date = string_handle(table_td[7].text)
        cupon_rate = string_handle(table_td[8].text)
        debut_trading_date_basic = string_handle(table_td[9].text)
        cupon_frequency = string_handle(table_td[10].text)
        maturity_date = string_handle(table_td[11].text)
        security_catagory = string_handle(table_td[12].text)
        electronic_share_basic = string_handle(table_td[13].text)
        year_basis = string_handle(table_td[14].text)
        type_of_instrument = string_handle(table_td[1].text)
        face_par_value = string_handle(table_td[4].text)
        market_lot = string_handle(table_td[5].text)
        total_outstanding_security = string_handle(table_td[2].text)
        sector = string_handle(table_td[3].text)

        return {
            "issuer": issuer,
            "tenure": tenure,
            "issue_date": issue_date,
            "cupon_rate": cupon_rate,
            "debut_trading_date_basic": debut_trading_date_basic,
            "cupon_frequency": cupon_frequency,
            "maturity_date": maturity_date,
            "security_catagory": security_catagory,
            "electronic_share_basic": electronic_share_basic,
            "year_basis": year_basis,
            "authorized_capital": "N/A",
            "debut_trading_date": "N/A",
            "paid_up_capital": "N/A",
            "type_of_instrument": type_of_instrument,
            "face_par_value": face_par_value,
            "market_lot": market_lot,
            "total_outstanding_security": total_outstanding_security,
            "sector": sector
        }


def address_table(table_td, company_type_td):
    if company_type_td == False:
        address_head_office = string_handle(table_td[2].text)
        address_factory = string_handle(table_td[4].text)
        contact_phone = string_handle(table_td[6].text)
        fax = string_handle(table_td[8].text)
        email = string_handle(table_td[10].text)
        web = string_handle(table_td[12].text)
        company_secretary_name = string_handle(table_td[14].text)
        secretary_cell_no = string_handle(table_td[16].text)
        secretary_telephone_no = string_handle(table_td[18].text)
        secratary_email = string_handle(table_td[20].text)

        return {
            "address_head_office": address_head_office,
            "address_factory": address_factory,
            "address_issuer": "N/A",
            "concern_department": "N/A",
            "contact_phone": contact_phone,
            "fax": fax,
            "email": email,
            "web": web,
            "company_secretary_name": company_secretary_name,
            "secretary_cell_no": secretary_cell_no,
            "secretary_telephone_no": secretary_telephone_no,
            "secratary_email": secratary_email
        }

    else:
        address_issuer = string_handle(table_td[1].text)
        concern_department = string_handle(table_td[5].text)
        contact_phone = string_handle(table_td[7].text)
        email = string_handle(table_td[9].text)
        web = string_handle(table_td[3].text)

        return {
            "address_head_office": "N/A",
            "address_factory": "N/A",
            "address_issuer": address_issuer,
            "concern_department": concern_department,
            "contact_phone": contact_phone,
            "fax": "N/A",
            "email": email,
            "web": web,
            "company_secretary_name": "N/A",
            "secretary_cell_no": "N/A",
            "secretary_telephone_no": "N/A",
            "secratary_email": "N/A"
        }
