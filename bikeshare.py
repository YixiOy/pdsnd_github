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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Would you like to see data for Chicago, New York or Washington?")).lower()
    while  city not in {'chicago', 'new york', 'washington'}:
        city = str(input("Please enter the valid city: ")).lower()

    # get user input for month (all, january, february, ... , june)
    month = str(input("Which month would you like to filter the data by? Please choose from all, january, february, march,april, may, june")).lower()
    while month not in {'all', 'january', 'february', 'march', 'april', 'may', 'june'}:
        month = str(input("Please enter the valid month: ")).lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Which day would you like to filter the date by? Please choose from all, monday, tuesday,...,sunday")).lower()
    while  day not in {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}:
        day = str(input("Please enter the valid day: ")).lower()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe most common month is {}'.format(popular_month))


    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('\nMost common day of week: ', popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost common start hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station is: ', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station is: ', popular_end_station)


    # display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).count().sort_values(by=['Start Station','End Station'], axis = 0).iloc[0, 'Start Station' : 'End Station']
    print('\nMost frequent combination of start station and end station trip is: ', popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    print('\nTotal travel time is: ', total_travel_time)


    # display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('\nAverage travel time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print (user_types) 


    # Display counts of gender
    gender = df['Gender'].value_counts()
    print (gender)


    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    recent_birth_year = df['Birth Year'].max()
    most_common_birth_year = df['Birth Year'].mode()[0]
    print('\nearliest birth year is: ', earliest_birth_year)
    print('\nmost recent birth year is: ', recent_birth_year)
    print('\nmost common year of birth is: ', most_common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
