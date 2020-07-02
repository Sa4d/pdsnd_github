import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        city=input("\n What city would you like to see, new york city, chicago or washington? ").lower()
        if (city=="new york city" or city=="chicago" or city=="washington"):
            break
        else:
            print("\nEnter one of the available options please")


    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        month=input("\n choose a month from january to june or all if you want: ").lower()
        if (month=="january" or month=="february" or month=="march" or month=="april" or month=="may" or month=="june" or month=="all"):
            break
        else:
            print("\nEnter one of the available options please")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day=input("\n choose a day of the week or you can choose all: ").lower()
        if (day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday" or day=="saturday" or day=="sunday" or day=="all" ):
            break
        else:
            print("\nEnter one of the available options please")

    print('-'*40)
    return city, month , day


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
    #loading data of city into dataframe
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #convert start time to date time

    df['End Time'] = pd.to_datetime(df['End Time'])
    #convert end time to date time

    #filter by month
    if month != 'all':
        df['month'] = df['Start Time'].dt.month

        #to get index of month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df.loc[df['month'] == month]

    #filter by day
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        df = df.loc[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # TO DO: display the most common month
    mc_month = df['Start Time'].dt.month.mode()[0]
    print("most common month: ", mc_month)

    # TO DO: display the most common day of week
    mc_day = df['Start Time'].dt.weekday_name.mode()[0]
    print("most common day: ", mc_day)

    # TO DO: display the most common start hour
    mc_hour = df['Start Time'].dt.hour.mode()[0]
    print("most common hour: ", mc_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station: ", df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("Most commonly used end station: ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip

    #combine start and end station and find most frequent combo
    station_combo = df['Start Station'] + " and " + df['End Station']
    mc_station = station_combo.value_counts().idxmax()

    print("Most frequent combination of start station and end station trip: ",mc_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])

    print("Total travel time: ", total_time/60, " minutes")

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_time/60, " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("earliest year of birth",df['Birth Year'].min())
    print("most recent year of birth",df['Birth Year'].max())
    print("most common year of birth",df['Birth Year'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day= get_filters()
        print(city)
        print(month)
        print(day)
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
