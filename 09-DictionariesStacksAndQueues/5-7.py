def hotels_list(hotels):
    return ', '.join(hotel['name'] for hotel in hotels)

def avg_price(hotels):
    total_price = sum(hotel['price'] for hotel in hotels)
    average = total_price / len(hotels)
    return round(average)

def compare_prices(hotels_KRK, hotels_SPT):
    krk_hotels = hotels_list(hotels_KRK)
    spt_hotels = hotels_list(hotels_SPT)

    avg_krk = avg_price(hotels_KRK)
    avg_spt = avg_price(hotels_SPT)

    print(f"Hotels in Krakow: {krk_hotels}")
    print(f"Average hotel price in Krakow: {avg_krk}")
    print(f"Hotels in Sopot: {spt_hotels}")
    print(f"Average hotel price in Sopot: {avg_spt}") 

    if avg_krk < avg_spt:
        print('cheaper in krakow')

    elif avg_krk < avg_spt:
        print('cheaper in sopot')

    else:
        print('equal') 

hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

# Call the function to compare prices
compare_prices(hotels_in_Krakow, hotels_in_Sopot)

