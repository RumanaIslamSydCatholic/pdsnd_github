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
    while True:
        city = input("Please enter a city name (chicago, new york city or washington): ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Please enter a valid city name (chicago, new york city or washington)")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter a month name or all for all months (all, january, february, ... , june): ")
        month = month.lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Please enter a valid month name (all, january, february, ... , june)")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a day of week or all for all days (all, monday, tuesday, ... sunday): ")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")
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

    # TO DO: display the most common month
    try:
        common_month = df['month'].mode()[0]
        print('most common month:', common_month)
    except: 
        print ('no most common month trip data available')

    # TO DO: display the most common day of week
    try:
        common_day = df['day_of_week'].mode()[0]
        print('most Common day:', common_day)
    except: 
        print ('no most common day of week trip data available')

    # TO DO: display the most common start hour
    try:
        df['hour'] = df['Start Time'].dt.hour
        common_start_hour = df['hour'].mode()[0]
        print('most common start hour:', common_start_hour)
    except: 
        print ('no most common start hour trip data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        common_start_station = df['Start Station'].mode()[0]
        print('most common start station:', common_start_station)
    except: 
        print ('no most commonly used start station trip data available')

    # TO DO: display most commonly used end station
    try: 
        common_end_station = df['End Station'].mode()[0]
        print('most common end station:', common_end_station)
    except: 
        print ('no most commonly used end station trip data available')

    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['frequent_combination_station'] = df['Start Station'] + " to " + df['End Station']
        common_combo_station = df['frequent_combination_station'].mode()[0]
        print('most frequent combination of start station and end station trip: ', common_combo_station)
    except: 
        print ('no most frequent combination of start station and end station trip data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_travel_time = df['Trip Duration'].sum()
        print('total travel time: ', total_travel_time)
    except: 
        print ('no total travel time data available')
        
    # TO DO: display mean travel time
    try:
        mean_travel_time = df['Trip Duration'].mean()
        print('mean travel time: ', mean_travel_time)
    except: 
        print ('no mean travel time data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('User Types:', '\n', user_types.to_string(), '\n')
    except: 
        print ('no user type data available')
    
    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('User Gender:', '\n', user_gender.to_string(), '\n')
    except:
        print('No gender data available')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('earliest year of birth: ', earliest_birth_year)
    except:
        print('No earliest year of birth data available')
        
    try:
        most_recent_birth_year = int(df['Birth Year'].max())
        print('most recent year of birth: ', most_recent_birth_year)
    except:
        print('No most recent year of birth data available')
        
    try:
        most_common__birth_year = int(df['Birth Year'].mode()[0])
        print('most common year of birth: ', most_common__birth_year)
    except:
        print('No most common year of birth data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data per users request."""
    print('\nDisplaying raw data...\n')
    start_time = time.time()    
    line_no = 1
    while True:  
        data = input('\nDisplay 5 lines of raw data? Enter yes or no.\n')
        if data.lower() == 'yes':
            try:
                raw_data = df[line_no:line_no+5]
                print('\n', raw_data, '\n')
                line_no = line_no+5
            except: 
                print('No raw data is available to display')
        else:
            break
    
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
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    
  #I completed this project with the help from Udacity python lessons and quiz solutions, from W3Schools site and stackoverflow site. #