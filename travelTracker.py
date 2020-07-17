travelledCountries = {}
historyTimes = ''

def displayPlaces(place):
    timesTraveled = 0
    for loc, times in place.items():
        timesTraveled += times
    if timesTraveled != 0:
        print("You've travelled to these places:")
        for loc, times in place.items():
            print(f'{times} times to {loc}')
        print(f"So far, you've travelled {timesTraveled} times!")
    else:
        print('You haven\'t travelled anywhere yet...')

def addtoHistory(country,times):
    travelledCountries[str(country)] = times

while True:
    historyCountry = str(input('What country did you travel to? (Leave blank to quit / Type "history" to see where you\'ve been): '))
    if historyCountry == '':
        break
    elif historyCountry.lower() == 'history':
        displayPlaces(travelledCountries)
    else:
        while historyTimes == '':
            historyTimes = int(input('How many times have you gone there?: '))
        addtoHistory(historyCountry,historyTimes)
        historyTimes = ''
        again=input('Country history database updated. Try again?:')
        if again == 'no':
            break




# displayPlaces(travelledCountries)
