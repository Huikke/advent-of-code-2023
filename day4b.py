total_cards = 0

with open("day4_data.txt") as data:
    data = data.readlines()
    card_i = 0
    card_copies = [1 for line in data]

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

        j = 1
        for your_number in your_numbers:
            if your_number in winning_numbers:
                card_copies[card_i + j] += card_copies[card_i]
                j += 1

        total_cards += card_copies[card_i]
        card_i += 1

print(total_cards)