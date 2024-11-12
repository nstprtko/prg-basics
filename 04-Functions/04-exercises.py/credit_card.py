def hide(credit_card):
    credit_card_str = str(credit_card)
    first_part = credit_card_str[:4]
    last_part = credit_card_str [-4:]
    middle_part = credit_card_str[4:-4]

    blurred_number = first_part + middle_part.replace(middle_part, "*" * len(middle_part))

    return blurred_number