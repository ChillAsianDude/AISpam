    # Convert to lowercase and strip leading/trailing whitespaces
    value = value.strip().lower()

    # Label anything with 'scam' or 'suspicious' as 'scam'
    if 'scam' in value or 'suspicious' in value:
        return 'scam'
    # Label legitimate variations as 'legitimate'
    elif 'legitimate' in value:
        return 'legitimate'
    # Otherwise, label as 'neutral'
    elif 'neutral' in value:
        return 'neutral'
    else:
        return 'neutral'  # Assign to 'neutral' if it doesn't fall into other categories