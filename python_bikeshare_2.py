import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

##to do next
##put 'break' clauses into the validation while loops in function get_filters
##check if the city intput


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


    city = input("What city would you like to analyze? Name city - Chicago, New York City or Washington: ").lower()
    while city not in('chicago', 'new york city', 'washington'):
        print('You got it wrong pls try again')
        city = input("What city would you like to analyze? Name city - Chicago, New York City or Washington ").lower()


    # get user input for month (all, january, february, ... , june)
    month = input("What month would you like to analyze? Name one month, or type 'All'. Only January to June are available ").lower()
    while month not in('january', 'febuary', 'march', 'april', 'may', 'june','all'):
        print('that\'s not a month - remember only first 6 month are available')
        month = input("What month would you like to analyze? Name one month, or type 'All'. Only January to June are available ").lower()

    #get day input
    day = input("What day of week would you like to analyze? Name one day, or type 'All' ").lower()
    while day not in('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print('that\'s not a day: please try again')
        day = input("WHat day of the week would you like to analyze? Name on day or type 'all'")


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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

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

    ##clean up column headings
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    ##use mode
    print("the most common month for bike hire is: ")
    print(df.month.mode().iloc[0])

    # display the most common day of week
    ##today print days out as day instead of number
    print("the most common day of the week is: ")
    print(df.day_of_week.mode().iloc[0])

    # display the most common start hour
    print("the most common start hour is: ")
    print(df.start_time.mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    ##clean up column headings
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    """Displays statistics on the most popular stations and trip."""

        #<class 'pandas.core.frame.DataFrame'>
        #Int64Index: 76022 entries, 0 to 299985
        #Data columns (total 11 columns):
        #unnamed:_0       76022 non-null int64
        #start_time       76022 non-null datetime64[ns]
        #end_time         76022 non-null object
        #trip_duration    76022 non-null int64
        #start_station    76022 non-null object
        #end_station      76022 non-null object
        #user_type        76022 non-null object
        #gender           67387 non-null object
        #birth_year       67629 non-null float64
        #month            76022 non-null int64
        #day_of_week      76022 non-null object
        #dtypes: datetime64[ns](1), float64(1), int64(3), object(6)



    #print info on DataFrame
    print('\n \n most current state of dataframe info as follows: \n')
    df.info()

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # display most commonly used start station
    print('\nThe most commonly used start station is: ')
    print(df.start_station.mode().iloc[0])


    # display most commonly used end station
    print('\nThe most commonly used end station is: ')
    print(df.end_station.mode().iloc[0])

    # display most frequent combination of start station and end station trip
    print('\nThe most frequent combo of start and end station is: ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    ##clean up column headings
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nThe total travel time is: ')
    print(df.trip_duration.sum())

    # display mean travel time
    print('\nThe mean travel time is: ')
    print(df.trip_duration.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def tidy_data(df):
    #"""A function to tidy the data for review analysis."""

    ##clean up column headings
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    #if city != 'washington':
        #set birth_year column as Int64 - Moved to tidy_data(df) function
    #    df['birth_year'] = df['birth_year'].astype(pd.Int64Dtype())

def user_stats(df):
    """Displays statistics on bikeshare users."""

    ##clean up column headings - this has been moved to tidy_data(df) function
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    #set birth_year column as Int64 - Moved to tidy_data(df) function (removed since doesn't work for Washington)
    df['birth_year'] = df['birth_year'].astype(pd.Int64Dtype())

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\n\nCount of user type as follows: ")
    print(df.groupby('user_type').count())

    ## TO DO - this paused program... I'm guessing with the Y axis code
    ##df.plot(x ='user_type', y=('user_type').count('user_type'), kind = 'bar')

    # Display counts of gender
    print("\n\nCount of gender as follows: ")
    print(df.groupby('gender').size())

    # Display earliest, most recent, and most common year of birth
    print('\n\nEarliest year of birth:')
    min_yob = df.birth_year.min()
    print(min_yob)

    print('\n\nMax year of birth: ')
    max_yob = df.birth_year.max()
    print(max_yob)

    print('\n\nMost common year of birth: ')
    mod_yob = df.birth_year.mode().iloc[0]
    print(mod_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    #print first 5 rows of df
    show_5rows = input('Would you like to see the first five rows? Yes?  ').lower()

    #variables to decide which 5 rows to print.
    x = 0
    y = 5

    #while loop to specify what to print

    while show_5rows == 'yes':
        print(df.iloc[x:y])
        x += 5
        y += 5
        print(x)
        print(y)
        show_5rows = input('Would you like to see the next five rows? Yes or No?  ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        if city == 'washington':
            tidy_data(df)
            time_stats(df)
            station_stats(df)
            print("\nNo user stats are available for Washington")
            trip_duration_stats(df)
            display_raw_data(df)

        else:
            tidy_data(df)
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
