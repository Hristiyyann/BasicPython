words_second_place = ['AA', 'AB', 'AK', 'AM', 'AH', 'AP', 'AC', 'AT', 'AX',
                      'BA', 'BB', 'BK', 'BM', 'BH', 'BP', 'BC', 'BT', 'BX',
                      'KA', 'KB', 'KK', 'KM', 'KH', 'KP', 'KC', 'KT', 'KX',
                      'MA', 'MB', 'MK', 'MM', 'MH', 'MP', 'MC', 'MT', 'MX',
                      'HA', 'HB', 'HK', 'HM', 'HH', 'HP', 'HC', 'HT', 'HX',
                      'PA', 'PB', 'PK', 'PM', 'PH', 'PP', 'PC', 'PT', 'PX',
                      'CA', 'CB', 'CK', 'CM', 'CH', 'CP', 'CC', 'CT', 'CX',
                      'TA', 'TB', 'TK', 'TM', 'TH', 'TP', 'TC', 'TT', 'TX',
                      'XA', 'XB', 'XK', 'XM', 'XH', 'XP', 'XC', 'XT', 'XX',
                      ]
words_first_place = ['A', 'B', 'K', 'X', 'M', 'E', 'P', 'CA', 'CB', 'CO', 'PB', 'PA', 'CC', 'T', 'H', 'TX', 'BH', 'BP',
                     'PK', 'CM', 'Y', 'CT', 'EH', 'CH', 'EB', 'OB', 'PP']

words_first_place.sort()

count = 0

for first_letters in words_first_place:
    for second_letters in words_second_place:
        for numbers in range(0, 10000):
            count += 1
            if numbers < 10:
                print(f'{first_letters} 000{numbers} {second_letters}')
            elif numbers < 100:
                print(f'{first_letters} 00{numbers} {second_letters}')
            elif 100 <= numbers < 1000:
                print(f'{first_letters} 0{numbers} {second_letters}')
            else:
                print(f'{first_letters} {numbers} {second_letters}')


print(count)
