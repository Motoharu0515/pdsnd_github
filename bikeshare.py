import time
import pandas as pd
import numpy as np
import statistics as stats


CITY_DATA =  { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (qchicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if not city in ['chicago', 'new york city', 'washington']:
            print('Sorry, it is not in the choice. Choose again')
            continue
        else:
            print(city)
            break
    dff = pd.read_csv(CITY_DATA[city])
    a = 5
    while True:
        answer = input('Do you want to see {} lines of raw data? Yes or No?'.format(a)).lower()
        if answer == 'yes':
            print(dff.head(a))
            a += 5
        elif answer == 'no':
            break

    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('\nWhich month? January, February, March, April, May, June, or all?').lower()
        if month in month_list:
            month = month_list.index(month) + 1
            print(month)
            break
        else:
            if month == 'all':
                print(all)
                break
            else:
                print('Sorry, choose again please')
                continue

            continue


    while True:
        day = input('\nWhich day of week or all?').title()
        if day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']:
            print('Sorry, choose again')
            continue
        else:
            print(day)
            break


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print('\nThe most common month: ', common_month)
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()
    print('\nThe most common day of week: ', common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()
    print('\nThe most common start hour is {}.'.format('common_start_hour'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station is {}.'.format(str(df['Start Station'].mode()[0])))

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('\nMost frequent combination of start station and end station trip: ', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('total travel time: ', total_time)
    # TO DO: display mean travel time
    mean_time = stats.mean(df['Trip Duration'])
    print('\nmean travel time: ', mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types: ', user_types)


    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print('\nCounts of gender: ', gender_type)
    except:
        print('\nCounts of gender: No data')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].min()
        print('\nEarliest year of birth: ', earliest_birthyear)

        most_recent_birthyear = df['Birth Year'].max()
        print('\nMost recent year of birth: ', most_recent_birthyear)

        most_common_birthyear =  df['Birth Year'].mode()[0]
        print('\nMost common year of birth: ', most_common_birthyear)
    except:
        print('\nYear of birth: No data')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
