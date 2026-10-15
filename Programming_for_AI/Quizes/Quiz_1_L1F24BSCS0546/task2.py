def analyze_inventory(stock_data, min_value):

    calculate_total_value = lambda data: float(data.split(":")[2]) * float(data.split(":")[3])
    
    result = [
        tuple(
            (
                data.split(':')[0], [data.split(":")[1], calculate_total_value(data)]
            )
        )
        for data in stock_data
        if calculate_total_value(data) > min_value
    ]
    
    result = sorted(result, reverse=False, key=lambda x: x[1][0])
    
    final_result = [
            dict(
                {
                    i[0]: i[1]
                }
            )
            for i in result
        ]
    
    return final_result

stock_data = ["A1:Office:10:50", "B2:Hardware:100:2", "C3:Office:5:10", "D4:Hardware:50:20", "D5:Accounts:20:80"]

print(analyze_inventory(stock_data, 50))