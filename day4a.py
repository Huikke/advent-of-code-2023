total_points = 0

with open("day4_data.txt") as data:
    for line in data:
        scratch_card = line.strip().split(" ")
        
        i = 0
        while i < len(scratch_card):
            if scratch_card[i].isdigit():
                scratch_card[i] = int(scratch_card[i])
                i += 1
            else:
                del scratch_card[i]
        
        winning_numbers = scratch_card[:10]
        your_numbers = scratch_card[10:]

        points = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2
        
        total_points += points

print(total_points)