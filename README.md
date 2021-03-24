
- Asks user to specify a city, month, and day to analyze.
	- Returns:
        - (str) city - name of the city to analyze
        - (str) month - name of the month to filter by, or "all" to apply no month filter
        - (str) day - name of the day of week to filter by, or "all" to apply no day filter

- Loads data for the specified city and filters by month and day if applicable.
  	- Args:
        - (str) city - name of the city to analyze
        - (str) month - name of the month to filter by, or "all" to apply no month filter
        - (str) day - name of the day of week to filter by, or "all" to apply no day filter
    - Returns:
        - df - Pandas DataFrame containing city data filtered by month and day

- Displays statistics on the most frequent times of travel.
	- display the most common month
	- display the most common day of week
	- display the most common start hour

- Displays statistics on the most popular stations and trip.
	- display most commonly used start station
	- display most commonly used end station
	- display most frequent combination of start station and end station trip

- Displays statistics on the total and average trip duration.
	- display total travel time
	- display mean travel time

- Displays statistics on bikeshare users.
	- display counts of user types
	- display counts of gender
	- display earliest, most recent, and most common year of birth