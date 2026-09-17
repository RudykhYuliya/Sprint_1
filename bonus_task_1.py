types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(tickets):
    seen = set()
    unique_tickets = {}

    for level in sorted(tickets):
        unique_list = []
        for ticket in tickets[level]:
            if ticket not in seen:
                unique_list.append(ticket)
                seen.add(ticket)
        unique_tickets[level] = unique_list

    return unique_tickets

def group_tickets_by_type(types, tickets):
    cleaned = remove_duplicates(tickets)
    result = {}
    for level, type_name in types.items():
        result[type_name] = cleaned[level]
    return result

tickets_by_type = group_tickets_by_type(types, tickets)
print(tickets_by_type)
    