import math

amount_banknotes = [1, 10, 100, 300]
list_banknotes_needed = [0, 0, 0, 0]
banknotes = [100, 50, 20, 10]
account_balance = 2000
answer = 'yes'


def inform_bank(banknote_type):
    print('need more money (%s bills)' % banknote_type)


withdraw_sum = int(input('How much money do you want to withdraw? '))
informed_missing_banknotes = []
while answer == 'yes':
    if withdraw_sum <= account_balance:
        index_value = 0

        while withdraw_sum > 0:
            chosen_banknote = banknotes[index_value]

            if index_value > len(banknotes):
                print('not enough bills')
                break

            else:
                banknotes_needed = math.floor(withdraw_sum / chosen_banknote)
                if banknotes_needed > 0:

                    banknotes_found = False
                    while not banknotes_found:
                        if amount_banknotes[index_value] >= banknotes_needed:
                            amount_withdrawn = chosen_banknote * banknotes_needed

                            withdraw_sum -= amount_withdrawn

                            list_banknotes_needed[index_value] += banknotes_needed
                            amount_banknotes[index_value] -= banknotes_needed
                            index_value += 1
                            banknotes_found = True

                        else:
                            banknotes_needed -= 1
                            if not index_value in informed_missing_banknotes:
                                informed_missing_banknotes.append(index_value)
                                inform_bank(banknotes[index_value])
                            if banknotes_needed == 0:
                                index_value += 1
                                break

                else:
                    index_value += 1

        index_banknotes = 0
        print(list_banknotes_needed)

        for i in banknotes:
            print(i * list_banknotes_needed[index_banknotes])
            index_banknotes += 1
        break
    else:
        print('Not enough money on your account')
        answer = input('Do you want to choose another sum? ("yes" "no")')
        if answer == 'yes':
            withdraw_sum = int(input('How much money do you want to withdraw? '))
        else:
            print('Thanks for using this ATM')
            break
