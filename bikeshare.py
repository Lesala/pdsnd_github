import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
week_days = ['monday', 'tuesday', 'wednesday', 'thursdays', 'friday', 'saturday', 'sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze..

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_user_validator("Would you like to explore data for chicago, new york city or washington?\n", 'c')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_user_validator("To view data by month kindly enter name of the month to filter from (january, february, march, april, may, june) otherwise enter 'all'\n", 'm')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_user_validator("To view data by day kindly enter name of day to filter from (monday, tuesday, wednesday, thursday, friday, saturday, sunday) otherwise enter 'all'\n", 'd')

    print('-'*40)
    return city, month, day
def input_user_validator(user_input, input_type):
        while True:
                input_user_entered=input(user_input).lower()
                try:
                    if input_user_entered in ['chicago','new york city', 'washington'] and input_type == 'c':
                        break
                    elif input_user_entered in months and input_type == 'm':
                        break
                    elif input_user_entered in week_days and input_type == 'd':
                        break
                    else:
                        if input_type == 'c':
                            print("Inoperative user input, user input must be: chicago, new york city or washington")
                        if input_type == 'm':
                            print("Inoperative user input, user input must be: january, february, march, april, may, june or all")
                        if input_type == 'd':
                            print("Inoperative user input, user input must be: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all")
                except ValueError:
                    print("You have entered an inappropriate input")
        return input_user_entered

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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        Months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = Months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_popular_month = months[df['month'].mode()[0] -1].title()

    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    most_popular_hour = df['hour'].mode()[0]
    print('the most common month is: ', most_popular_month)
    print('the most common day is: ', most_popular_day)
    print('the most common start hour is: ', most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_route = df.groupby(['Start Station', 'End Station']).count()

    print('most commonly used start station is: ', most_popular_end_station)
    print('most commonly used end station is: ', most_popular_end_station)
    print('Most Commonly used combination of start station and end station trip:', most_frequent_route)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('total travel time is: ', total_travel_time)
    print('mean travel time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('user types are: ', user_type_count)

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df["Gender"].value_counts().to_frame()
        print("user gender:\n", counts_of_gender)
    except:
        print("no data available about gender for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earlies_year_of_birth = int(df["Birth Year"].min())
        print("earliest year of birth is:", earlies_year_of_birth)

        most_recent_year_of_birth = int(df["Birth Year"].max())
        print("most recent year of birth  is:", most_recent_year_of_birth)

        most_common_year_of_birth = int(df["Birth Year"].mode())
        print("most common year of birth is:", most_common_year_of_birth)
    except:
        print("no data available about birth year for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    row_view = 5
    start_loc = 0
    end_loc = row_view - 1

    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data.lower()  == "yes":
            print('\n    Displaying rows {} to {}:'.format(start_loc + 1, end_loc + 1))

            print('\n', df.iloc[start_loc : end_loc + 1])
            start_loc += row_view
            end_loc += row_view

            print('\n    Would you like to see the next {} rows?'.format(row_view))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
