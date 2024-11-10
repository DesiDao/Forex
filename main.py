def generate_currency_positions(bank,
                                current_bid,
                                net_position,
                                take_profit,
                                margin_multiplier=19.75):
    
    position = 'Buy' if take_profit > net_position else 'Sell'
    margin = margin_multiplier * current_bid
    equity = bank - margin
    positions = []
    
    while net_position < take_profit:
            #print(equity, target)

            pips_to_take_profit = 125.5 / current_bid
            #print(current_bid, pips_to_take_profit)
            
            take_profit_position = round(net_position + (pips_to_take_profit * 0.001), 5)
            current_bid += 5
            equity += 25
            margin = margin_multiplier * current_bid
            #print(net_position, take_profit_position)
            positions.append({
                'Total Bid': current_bid,
                'Net Position': take_profit_position,
                'Equity' : equity,
                'Take Profit': take_profit
            })
            net_position = take_profit_position

    return positions


positions = generate_currency_positions(bank=1040.27,
                                        current_bid=37.00,
                                        net_position=0.65925,
                                        take_profit=0.68200)

for i, position in enumerate(positions, start=1):
    print(f"Position {i}: {position}")

print(positions)
