'''
Data cleaning and final dataframe creation:

Summary:

a) FIFA database

- import the FIFA database of each year, which includes information about every player in the game
- Keep only the columns that will be useful and usable in our final model
- Keep only the players that play in the English Premier League
- Group the players by team
- Compute the mean attributes for each team, using individual information of each player in the team
- Repeat for each year ( Season 14/15 --> Season 18/19)
- Save all the new dataframes in a folder

b) Matches database

- Create new columns, where the avgs coming from the FIFA databse will be incorporated
- Normalize the club names for the two databases, since the names are not the same
- Manually add (through a big for loop) the avgs from the FIFA database to the corresponding match. Each avg must be added in the column
 'Home' or 'Away', depending on if the team play at home or away
- Repeat for each Premier League season


c) Create dynamic statistics using in-games stats for each team

- 1) Compute the number of points of each team at the time of the match for a given Season (Points obtained before the match)
- Create a new dataframe to keeps track of the points and cumulative points and control if the work was
  executed correctly by looking the stands on internet
- 2) Compute the goals scored by each team
- 3) Compute the goals scored until the match date
- Add all the statistics to the main dataframe using a dynamic method (we found this method in the end, which
 simplified our work tremendously!)


d) Merge all the seasons into one single final dataframe
- save the final dataframe

'''


import pandas as pd
import numpy as np
from collections import defaultdict
from scipy import _lib

################################################
# a) FIFA DATABASE
################################################

#########
#FIFA 15
#########


fifa15 = pd.read_csv('fifa15_players.csv', sep=';', engine = 'python')

# Drop the attribute that are not useful for our analysis

unusable_col = [ 'long_name', 'dob',
				'weight_kg','league_rank','player_positions','preferred_foot', 'weak_foot', 'skill_moves', 'work_rate', 'player_url']

players_14_15 = fifa15.drop(unusable_col, axis = 1)

# Keep only Premier League players

pl_players_14_15 = players_14_15.loc[players_14_15["league_name"] == "English Premier League"]


# Group all the players by team

teams_14_15 = pl_players_14_15.club_name.unique()

teams1415 = teams_14_15.tolist()


players_teams_1415 = pl_players_14_15.sort_values(by = ['club_name'], ascending = True)


# Compute average values per team

avg_1415 = players_teams_1415.groupby("club_name").mean()

#########
#FIFA 16
#########


fifa16 = pd.read_csv('fifa16_players.csv', sep=';', engine = 'python')

# Drop the attribute that are not useful for our analysis

unusable_col = [ 'long_name', 'dob',
				'weight_kg','league_rank','player_positions','preferred_foot', 'weak_foot', 'skill_moves', 'work_rate', 'player_url']

players_15_16 = fifa16.drop(unusable_col, axis = 1)

# Keep only Premier League players

pl_players_15_16 = players_15_16.loc[players_15_16["league_name"] == "English Premier League"]

# Group all the players by team

teams_15_16 = pl_players_15_16.club_name.unique()

teams1516 = teams_15_16.tolist()


players_teams_1516 = pl_players_15_16.sort_values(by = ['club_name'], ascending = True)



# Compute average values per team

avg_1516 = players_teams_1516.groupby("club_name").mean()


#########
#FIFA 17
#########


fifa17 = pd.read_csv('fifa17_players.csv', sep=';', engine = 'python')

# Drop the attribute that are not useful for our analysis

unusable_col = [ 'long_name', 'dob',
				'weight_kg','league_rank','player_positions','preferred_foot', 'weak_foot', 'skill_moves', 'work_rate', 'player_url']

players_16_17 = fifa17.drop(unusable_col, axis = 1)

# Keep only Premier League players

pl_players_16_17 = players_16_17.loc[players_16_17["league_name"] == "English Premier League"]

# Group all the players by team

teams_16_17 = pl_players_16_17.club_name.unique()

teams1617 = teams_16_17.tolist()


players_teams_1617 = pl_players_16_17.sort_values(by = ['club_name'], ascending = True)



# Compute average values per team

avg_1617 = players_teams_1617.groupby("club_name").mean()


#########
#FIFA 18
#########


fifa18 = pd.read_csv('fifa18_players.csv', sep=';', engine = 'python')

# Drop the attribute that are not useful for our analysis

unusable_col = ['long_name', 'dob',
				'weight_kg','league_rank','player_positions','preferred_foot', 'weak_foot', 'skill_moves', 'work_rate', 'player_url']

players_17_18 = fifa18.drop(unusable_col, axis = 1)

# Keep only Premier League players

pl_players_17_18 = players_17_18.loc[players_17_18["league_name"] == "English Premier League"]

# Group all the players by team

teams_17_18 = pl_players_17_18.club_name.unique()

teams1718 = teams_17_18.tolist()


players_teams_1718 = pl_players_17_18.sort_values(by = ['club_name'], ascending = True)



# Compute average values per team

avg_1718 = players_teams_1718.groupby("club_name").mean()


#########
#FIFA 19
#########


fifa19 = pd.read_csv('fifa19_players.csv', sep=';', engine = 'python')

# Drop the attribute that are not useful for our analysis

unusable_col = ['long_name', 'dob',
				'weight_kg','league_rank','player_positions','preferred_foot', 'weak_foot', 'skill_moves', 'work_rate', 'player_url']

players_18_19 = fifa19.drop(unusable_col, axis = 1)

# Keep only Premier League players

pl_players_18_19 = players_18_19.loc[players_18_19["league_name"] == "English Premier League"]

# Group all the players by team

teams_18_19 = pl_players_18_19.club_name.unique()

teams1819 = teams_18_19.tolist()


players_teams_1819 = pl_players_18_19.sort_values(by = ['club_name'], ascending = True)


# Compute average values per team

avg_1819 = players_teams_1819.groupby("club_name").mean()

# Save the new dataframes in a folder

avgs = [avg_1415,avg_1516,avg_1617,avg_1718,avg_1819]
avgs_name = ['avg_1415.csv','avg_1516.csv','avg_1617.csv','avg_1718.csv','avg_1819.csv']


avg_1415.to_csv(avgs_name[0])
avg_1516.to_csv(avgs_name[1])
avg_1617.to_csv(avgs_name[2])
avg_1718.to_csv(avgs_name[3])
avg_1819.to_csv(avgs_name[4])


###################################################################################################

################################################
# a) Matches database
################################################


# import the databases with all the Premier League games


df14_15 = pd.read_csv('season-1415_csv.csv')
df15_16 = pd.read_csv('season-1516_csv.csv')
df16_17 = pd.read_csv('season-1617_csv.csv')
df17_18 = pd.read_csv('season-1718_csv.csv')
df18_19 = pd.read_csv('season-1819_csv.csv')


# Import the dataframes that we have created in the first part

avg_1415 = pd.read_csv('avg_1415.csv')
avg_1516 = pd.read_csv('avg_1516.csv')
avg_1617 = pd.read_csv('avg_1617.csv')
avg_1718 = pd.read_csv('avg_1718.csv')
avg_1819 = pd.read_csv('avg_1819.csv')

###############
# Season 14/15
###############

# Create the new columns to add into our initial df to add the information coming from the FIFA database

col_names = avg_1415.columns.tolist()

for name in col_names:
	df14_15[f'{name}_Home'] = np.nan
	df14_15[f'{name}_Away'] = np.nan



# correct the names of the clubs fow which the name is not the same in the two databases

names_col_df = sorted(df14_15["HomeTeam"].unique())

avg_1415["club_name"] = names_col_df

df14_15["club_name_Home"] = df14_15["HomeTeam"]
df14_15["club_name_Away"] = df14_15["AwayTeam"]


list_col = df14_15.columns[70:].tolist()

age_Home = []
age_Away = []
height_cm_Home = []
height_cm_Away = []
overall_Home = []
overall_Away = []
potential_Home = []
potential_Away = []
val_eur_Home = []
val_eur_Away = []
wage_eur_Home = []
wage_eur_Away = []
international_reputation_Home = []
international_reputation_Away = []


# Manually add the avg values to the main df

for match in df14_15.iloc:
	for line in avg_1415.iloc:
		if match["HomeTeam"] == line["club_name"]:
			age_Home.append(line["age"])
			height_cm_Home.append(line["height_cm"])
			overall_Home.append(line["overall"])
			potential_Home.append(line["potential"])
			val_eur_Home.append(line["value_eur"])
			wage_eur_Home.append(line["wage_eur"])
			international_reputation_Home.append(line["international_reputation"])
		if match["AwayTeam"] == line["club_name"]:
			age_Away.append(line["age"])
			height_cm_Away.append(line["height_cm"])
			overall_Away.append(line["overall"])
			potential_Away.append(line["potential"])
			val_eur_Away.append(line["value_eur"])
			wage_eur_Away.append(line["wage_eur"])
			international_reputation_Away.append(line["international_reputation"])


df14_15["age_Home"] = age_Home
df14_15["age_Away"] = age_Away
df14_15["height_cm_Home"] = height_cm_Home
df14_15["height_cm_Away"] = height_cm_Away
df14_15["overall_Home"] = overall_Home
df14_15["overall_Away"] = overall_Away
df14_15["potential_Home"] = potential_Home
df14_15["potential_Away"] = potential_Away
df14_15["value_eur_Home"] = val_eur_Home
df14_15["value_eur_Away"] = val_eur_Away
df14_15["wage_eur_Home"] = wage_eur_Home
df14_15["wage_eur_Away"] = wage_eur_Away
df14_15["international_reputation_Home"] = international_reputation_Home
df14_15["international_reputation_Away"] = international_reputation_Away


###############
# Season 15/16
###############

# Create the new columns to add into our initial df

col_names = avg_1516.columns.tolist()

for name in col_names:
	df15_16[f'{name}_Home'] = np.nan
	df15_16[f'{name}_Away'] = np.nan



# correct the names of the clubs fow which the name is not the same in the two databases

names_col_df = sorted(df15_16["HomeTeam"].unique())

avg_1516["club_name"] = names_col_df



df15_16["club_name_Home"] = df15_16["HomeTeam"]
df15_16["club_name_Away"] = df15_16["AwayTeam"]


list_col = df15_16.columns[70:].tolist()

age_Home = []
age_Away = []
height_cm_Home = []
height_cm_Away = []
overall_Home = []
overall_Away = []
potential_Home = []
potential_Away = []
val_eur_Home = []
val_eur_Away = []
wage_eur_Home = []
wage_eur_Away = []
international_reputation_Home = []
international_reputation_Away = []


# Manually add the avg values to the main df

for match in df15_16.iloc:
	for line in avg_1516.iloc:
		if match["HomeTeam"] == line["club_name"]:
			age_Home.append(line["age"])
			height_cm_Home.append(line["height_cm"])
			overall_Home.append(line["overall"])
			potential_Home.append(line["potential"])
			val_eur_Home.append(line["value_eur"])
			wage_eur_Home.append(line["wage_eur"])
			international_reputation_Home.append(line["international_reputation"])
		if match["AwayTeam"] == line["club_name"]:
			age_Away.append(line["age"])
			height_cm_Away.append(line["height_cm"])
			overall_Away.append(line["overall"])
			potential_Away.append(line["potential"])
			val_eur_Away.append(line["value_eur"])
			wage_eur_Away.append(line["wage_eur"])
			international_reputation_Away.append(line["international_reputation"])


df15_16["age_Home"] = age_Home
df15_16["age_Away"] = age_Away
df15_16["height_cm_Home"] = height_cm_Home
df15_16["height_cm_Away"] = height_cm_Away
df15_16["overall_Home"] = overall_Home
df15_16["overall_Away"] = overall_Away
df15_16["potential_Home"] = potential_Home
df15_16["potential_Away"] = potential_Away
df15_16["value_eur_Home"] = val_eur_Home
df15_16["value_eur_Away"] = val_eur_Away
df15_16["wage_eur_Home"] = wage_eur_Home
df15_16["wage_eur_Away"] = wage_eur_Away
df15_16["international_reputation_Home"] = international_reputation_Home
df15_16["international_reputation_Away"] = international_reputation_Away

df15_16= df15_16.dropna(how='all', axis=1)


###############
# Season 16/17
###############

# Create the new columns to add into our initial df

col_names = avg_1617.columns.tolist()

for name in col_names:
	df16_17[f'{name}_Home'] = np.nan
	df16_17[f'{name}_Away'] = np.nan


# correct the names of the clubs fow which the name is not the same in the two databases

names_col_df = sorted(df16_17["HomeTeam"].unique())

avg_1617["club_name"] = names_col_df


df16_17["club_name_Home"] = df16_17["HomeTeam"]
df16_17["club_name_Away"] = df16_17["AwayTeam"]


list_col = df16_17.columns[70:].tolist()

age_Home = []
age_Away = []
height_cm_Home = []
height_cm_Away = []
overall_Home = []
overall_Away = []
potential_Home = []
potential_Away = []
val_eur_Home = []
val_eur_Away = []
wage_eur_Home = []
wage_eur_Away = []
international_reputation_Home = []
international_reputation_Away = []

# Manually add the avg values to the main df

for match in df16_17.iloc:
	for line in avg_1617.iloc:
		if match["HomeTeam"] == line["club_name"]:
			age_Home.append(line["age"])
			height_cm_Home.append(line["height_cm"])
			overall_Home.append(line["overall"])
			potential_Home.append(line["potential"])
			val_eur_Home.append(line["value_eur"])
			wage_eur_Home.append(line["wage_eur"])
			international_reputation_Home.append(line["international_reputation"])
		if match["AwayTeam"] == line["club_name"]:
			age_Away.append(line["age"])
			height_cm_Away.append(line["height_cm"])
			overall_Away.append(line["overall"])
			potential_Away.append(line["potential"])
			val_eur_Away.append(line["value_eur"])
			wage_eur_Away.append(line["wage_eur"])
			international_reputation_Away.append(line["international_reputation"])


df16_17["age_Home"] = age_Home
df16_17["age_Away"] = age_Away
df16_17["height_cm_Home"] = height_cm_Home
df16_17["height_cm_Away"] = height_cm_Away
df16_17["overall_Home"] = overall_Home
df16_17["overall_Away"] = overall_Away
df16_17["potential_Home"] = potential_Home
df16_17["potential_Away"] = potential_Away
df16_17["value_eur_Home"] = val_eur_Home
df16_17["value_eur_Away"] = val_eur_Away
df16_17["wage_eur_Home"] = wage_eur_Home
df16_17["wage_eur_Away"] = wage_eur_Away
df16_17["international_reputation_Home"] = international_reputation_Home
df16_17["international_reputation_Away"] = international_reputation_Away

df16_17= df16_17.dropna(how='all', axis=1)

###############
# Season 17/18
###############

# Create the new columns to add into our initial df

col_names = avg_1718.columns.tolist()

for name in col_names:
	df17_18[f'{name}_Home'] = np.nan
	df17_18[f'{name}_Away'] = np.nan



# correct the names of the clubs fow which the name is not the same in the two databases

names_col_df = sorted(df17_18["HomeTeam"].unique())

avg_1718["club_name"] = names_col_df



df17_18["club_name_Home"] = df17_18["HomeTeam"]
df17_18["club_name_Away"] = df17_18["AwayTeam"]


list_col = df17_18.columns[70:].tolist()

age_Home = []
age_Away = []
height_cm_Home = []
height_cm_Away = []
overall_Home = []
overall_Away = []
potential_Home = []
potential_Away = []
val_eur_Home = []
val_eur_Away = []
wage_eur_Home = []
wage_eur_Away = []
international_reputation_Home = []
international_reputation_Away = []

# Manually add the avg values to the main df

for match in df17_18.iloc:
	for line in avg_1718.iloc:
		if match["HomeTeam"] == line["club_name"]:
			age_Home.append(line["age"])
			height_cm_Home.append(line["height_cm"])
			overall_Home.append(line["overall"])
			potential_Home.append(line["potential"])
			val_eur_Home.append(line["value_eur"])
			wage_eur_Home.append(line["wage_eur"])
			international_reputation_Home.append(line["international_reputation"])
		if match["AwayTeam"] == line["club_name"]:
			age_Away.append(line["age"])
			height_cm_Away.append(line["height_cm"])
			overall_Away.append(line["overall"])
			potential_Away.append(line["potential"])
			val_eur_Away.append(line["value_eur"])
			wage_eur_Away.append(line["wage_eur"])
			international_reputation_Away.append(line["international_reputation"])


df17_18["age_Home"] = age_Home
df17_18["age_Away"] = age_Away
df17_18["height_cm_Home"] = height_cm_Home
df17_18["height_cm_Away"] = height_cm_Away
df17_18["overall_Home"] = overall_Home
df17_18["overall_Away"] = overall_Away
df17_18["potential_Home"] = potential_Home
df17_18["potential_Away"] = potential_Away
df17_18["value_eur_Home"] = val_eur_Home
df17_18["value_eur_Away"] = val_eur_Away
df17_18["wage_eur_Home"] = wage_eur_Home
df17_18["wage_eur_Away"] = wage_eur_Away
df17_18["international_reputation_Home"] = international_reputation_Home
df17_18["international_reputation_Away"] = international_reputation_Away

df17_18= df17_18.dropna(how='all', axis=1)

###############
# Season 18/19
###############

# Create the new columns to add into our initial df

col_names = avg_1819.columns.tolist()

for name in col_names:
	df18_19[f'{name}_Home'] = np.nan
	df18_19[f'{name}_Away'] = np.nan


# correct the names of the clubs fow which the name is not the same in the two databases

names_col_df = sorted(df18_19["HomeTeam"].unique())

avg_1819["club_name"] = names_col_df


df18_19["club_name_Home"] = df18_19["HomeTeam"]
df18_19["club_name_Away"] = df18_19["AwayTeam"]


list_col = df18_19.columns[70:].tolist()

age_Home = []
age_Away = []
height_cm_Home = []
height_cm_Away = []
overall_Home = []
overall_Away = []
potential_Home = []
potential_Away = []
val_eur_Home = []
val_eur_Away = []
wage_eur_Home = []
wage_eur_Away = []
international_reputation_Home = []
international_reputation_Away = []

# Manually add the avg values to the main df

for match in df18_19.iloc:
	for line in avg_1819.iloc:
		if match["HomeTeam"] == line["club_name"]:
			age_Home.append(line["age"])
			height_cm_Home.append(line["height_cm"])
			overall_Home.append(line["overall"])
			potential_Home.append(line["potential"])
			val_eur_Home.append(line["value_eur"])
			wage_eur_Home.append(line["wage_eur"])
			international_reputation_Home.append(line["international_reputation"])
		if match["AwayTeam"] == line["club_name"]:
			age_Away.append(line["age"])
			height_cm_Away.append(line["height_cm"])
			overall_Away.append(line["overall"])
			potential_Away.append(line["potential"])
			val_eur_Away.append(line["value_eur"])
			wage_eur_Away.append(line["wage_eur"])
			international_reputation_Away.append(line["international_reputation"])


df18_19["age_Home"] = age_Home
df18_19["age_Away"] = age_Away
df18_19["height_cm_Home"] = height_cm_Home
df18_19["height_cm_Away"] = height_cm_Away
df18_19["overall_Home"] = overall_Home
df18_19["overall_Away"] = overall_Away
df18_19["potential_Home"] = potential_Home
df18_19["potential_Away"] = potential_Away
df18_19["value_eur_Home"] = val_eur_Home
df18_19["value_eur_Away"] = val_eur_Away
df18_19["wage_eur_Home"] = wage_eur_Home
df18_19["wage_eur_Away"] = wage_eur_Away
df18_19["international_reputation_Home"] = international_reputation_Home
df18_19["international_reputation_Away"] = international_reputation_Away

df18_19= df18_19.dropna(how='all', axis=1)


# Add a column 'Season...' to keep track of the Season in the main dataframe

df14_15["Div"] = "Season14_15"
df15_16["Div"] = "Season15_16"
df16_17["Div"] = "Season16_17"
df17_18["Div"] = "Season17_18"
df18_19["Div"] = "Season18_19"

###################################################################################################


##################################################################
# c) Create dynamic statistics using in-games stats for each team
##################################################################

###############
# Season 14/15
###############


## 1) Points obtained until the match

# Create a sub-dataframe to simplify the work

df14_15_stats = df14_15.iloc[:,:23]


squads_14_15 = (df14_15.HomeTeam.unique())

# Create a separate dataframe to keep track of the points for each team

dct_14_15_pts = {}
for squad in squads_14_15:
	dct_14_15_pts[f'{squad}'] = []

# Manually add the points for each team

for squad in squads_14_15:
	for line in df14_15_stats.iloc:
		if line["HomeTeam"] == squad:
			if line["FTR"] == "H":
				dct_14_15_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_14_15_pts[f'{squad}'].append(1)
			elif line["FTR"] == "A":
				dct_14_15_pts[f'{squad}'].append(0)

		if line["AwayTeam"] == squad:
			if line["FTR"] == "A":
				dct_14_15_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_14_15_pts[f'{squad}'].append(1)
			elif line["FTR"] == "H":
				dct_14_15_pts[f'{squad}'].append(0)



df_pts_14_15 = pd.DataFrame(dct_14_15_pts, columns = dct_14_15_pts.keys())


df14_15_stats["Home_cum_pts"] = np.nan
df14_15_stats["Away_cum_pts"] = np.nan

# Create a column that keeps track of cumulative points (for controlling purposes)

df_pts_14_15_cum = df_pts_14_15.apply(np.cumsum)
df_pts_14_15_xum_T = df_pts_14_15.transpose()

cols = df_pts_14_15.columns
col_team = list(cols)

# create a new dataframe for controlling purposes

dct_14_15_goals = {}
for squad in squads_14_15:
	dct_14_15_goals[f'{squad}'] = []



for squad in squads_14_15:
	for line in df14_15_stats.iloc:
		if line["HomeTeam"] == squad:
			dct_14_15_goals[f'{squad}'].append(line["FTHG"])

		if line["AwayTeam"] == squad:
			dct_14_15_goals[f'{squad}'].append(line["FTAG"])

## 2) goals scored

df_goals_14_15 = pd.DataFrame(dct_14_15_goals, columns = dct_14_15_goals.keys())

df_goals_14_15 = df_goals_14_15.apply(np.cumsum)
df_goals_14_15_T = df_goals_14_15.transpose()

df14_15_stats["Home_cum_golas"] = np.nan
df14_15_stats["Away_cum_golas"] = np.nan

# Add the statistics to the main dataframe (pts, pts for the last five games, goals)

teamTracking = defaultdict(lambda: { 'pts' : 0, 'games' : 0, 'goals':0,'goalsagainst':0, 'recent': [], 'recentHome': [], 'recentAway': []} )



# Add new columns
df14_15['PointsHome'] = ''
df14_15['PointsAway'] = ''
df14_15['GamesHome'] = ''
df14_15['GamesAway'] = ''
df14_15['GoalsHome'] = ''
df14_15['GoalsAway'] = ''
df14_15['GoalsagainstHome'] = ''
df14_15['GoalsagainstAway'] = ''



for n,row in df14_15.iterrows():

	home = row['HomeTeam']
	away = row['AwayTeam']

	# Write tracking data before altering
	df14_15.at[n, 'PointsHome'] = teamTracking[home]['pts']
	df14_15.at[n, 'PointsAway'] = teamTracking[away]['pts']
	df14_15.at[n, 'GamesHome'] = teamTracking[home]['games']
	df14_15.at[n, 'GamesAway'] = teamTracking[away]['games']
	df14_15.at[n, 'GoalsHome'] = teamTracking[home]['goals']
	df14_15.at[n, 'GoalsAway'] = teamTracking[away]['goals']
	df14_15.at[n, 'GoalsagainstHome'] = teamTracking[home]['goalsagainst']
	df14_15.at[n, 'GoalsagainstAway'] = teamTracking[away]['goalsagainst']


	# Update tracking data
	teamTracking[home]['games'] += 1
	teamTracking[away]['games'] += 1

	if row['FTR'] == 'H' :
		teamTracking[home]['pts'] += 3
	elif row['FTR'] == 'A' :
		teamTracking[away]['pts'] += 3
	elif row['FTR'] == 'D' :
		teamTracking[home]['pts'] += 1
		teamTracking[away]['pts'] += 1

	teamTracking[home]['goals'] += row['FTHG']
	teamTracking[away]['goals'] += row['FTAG']
	teamTracking[home]['goalsagainst'] += row['FTAG']
	teamTracking[away]['goalsagainst'] += row['FTHG']



# Write tracking data before altering
	df14_15.at[n, 'TotalLast5Home'] = sum(teamTracking[home]['recent'][-5:])
	df14_15.at[n, 'TotalLast5Away'] = sum(teamTracking[away]['recent'][-5:])
	df14_15.at[n, 'Last5WhenHome'] = sum(teamTracking[home]['recentHome'][-5:])
	df14_15.at[n, 'Last5WhenAway'] = sum(teamTracking[away]['recentAway'][-5:])



	ptsHome = 0
	ptsAway = 0
	if row['FTR'] == 'H':
		ptsHome = 3
	elif row['FTR'] == 'A':
		ptsAway = 3
	elif row['FTR'] == 'D':
		ptsHome = 1
		ptsAway = 1

	teamTracking[home]['pts'] += ptsHome
	teamTracking[home]['recent'].append(ptsHome)
	teamTracking[home]['recentHome'].append(ptsHome)

	teamTracking[away]['pts'] += ptsAway
	teamTracking[away]['recent'].append(ptsAway)
	teamTracking[away]['recentAway'].append(ptsAway)


###############
# Season 15/16
###############

df15_16_stats = df15_16.iloc[:,:23]


## 1) Points obtained until the match

# Create a sub-dataframe to simplify the work

squads_15_16 = (df15_16.HomeTeam.unique())

dct_15_16_pts = {}
for squad in squads_15_16:
	dct_15_16_pts[f'{squad}'] = []

# Manually add the points for each team

for squad in squads_15_16:
	for line in df15_16_stats.iloc:
		if line["HomeTeam"] == squad:
			if line["FTR"] == "H":
				dct_15_16_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_15_16_pts[f'{squad}'].append(1)
			elif line["FTR"] == "A":
				dct_15_16_pts[f'{squad}'].append(0)

		if line["AwayTeam"] == squad:
			if line["FTR"] == "A":
				dct_15_16_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_15_16_pts[f'{squad}'].append(1)
			elif line["FTR"] == "H":
				dct_15_16_pts[f'{squad}'].append(0)


# Keep track of the points for controlling purposes

df_pts_15_16 = pd.DataFrame(dct_15_16_pts, columns = dct_15_16_pts.keys())


df15_16_stats["Home_cum_pts"] = np.nan
df15_16_stats["Away_cum_pts"] = np.nan



df_pts_15_16_cum = df_pts_15_16.apply(np.cumsum)
df_pts_15_16_xum_T = df_pts_15_16.transpose()


cols = df_pts_15_16.columns
col_team = list(cols)


## 2) Goals scored

dct_15_16_goals = {}
for squad in squads_15_16:
	dct_15_16_goals[f'{squad}'] = []


for squad in squads_15_16:
	for line in df15_16_stats.iloc:
		if line["HomeTeam"] == squad:
			dct_15_16_goals[f'{squad}'].append(line["FTHG"])

		if line["AwayTeam"] == squad:
			dct_15_16_goals[f'{squad}'].append(line["FTAG"])



df_goals_15_16= pd.DataFrame(dct_15_16_goals, columns = dct_15_16_goals.keys())

df_goals_15_16 = df_goals_15_16.apply(np.cumsum)
df_goals_15_16_T = df_goals_15_16.transpose()

df15_16_stats["Home_cum_golas"] = np.nan
df15_16_stats["Away_cum_golas"] = np.nan


# Add the statistics to the main dataframe


teamTracking = defaultdict(lambda: { 'pts' : 0, 'games' : 0, 'goals':0, 'goalsagainst': 0, 'recent': [], 'recentHome': [], 'recentAway': []} )



# Add new columns
df15_16['PointsHome'] = ''
df15_16['PointsAway'] = ''
df15_16['GamesHome'] = ''
df15_16['GamesAway'] = ''
df15_16['GoalsHome'] = ''
df15_16['GoalsAway'] = ''
df15_16['GoalsagainstHome'] = ''
df15_16['GoalsagainstAway'] = ''


for n,row in df15_16.iterrows():

	home = row['HomeTeam']
	away = row['AwayTeam']

	# Write tracking data before altering
	df15_16.at[n, 'PointsHome'] = teamTracking[home]['pts']
	df15_16.at[n, 'PointsAway'] = teamTracking[away]['pts']
	df15_16.at[n, 'GamesHome'] = teamTracking[home]['games']
	df15_16.at[n, 'GamesAway'] = teamTracking[away]['games']
	df15_16.at[n, 'GoalsHome'] = teamTracking[home]['goals']
	df15_16.at[n, 'GoalsAway'] = teamTracking[away]['goals']
	df15_16.at[n, 'GoalsagainstHome'] = teamTracking[home]['goalsagainst']
	df15_16.at[n, 'GoalsagainstAway'] = teamTracking[away]['goalsagainst']


	# Update tracking data
	teamTracking[home]['games'] += 1
	teamTracking[away]['games'] += 1

	if row['FTR'] == 'H' :
		teamTracking[home]['pts'] += 3
	elif row['FTR'] == 'A' :
		teamTracking[away]['pts'] += 3
	elif row['FTR'] == 'D' :
		teamTracking[home]['pts'] += 1
		teamTracking[away]['pts'] += 1

	teamTracking[home]['goals'] += row['FTHG']
	teamTracking[away]['goals'] += row['FTAG']
	teamTracking[home]['goalsagainst'] += row['FTAG']
	teamTracking[away]['goalsagainst'] += row['FTHG']




# Write tracking data before altering
	df15_16.at[n, 'TotalLast5Home'] = sum(teamTracking[home]['recent'][-5:])
	df15_16.at[n, 'TotalLast5Away'] = sum(teamTracking[away]['recent'][-5:])
	df15_16.at[n, 'Last5WhenHome'] = sum(teamTracking[home]['recentHome'][-5:])
	df15_16.at[n, 'Last5WhenAway'] = sum(teamTracking[away]['recentAway'][-5:])



	ptsHome = 0
	ptsAway = 0
	if row['FTR'] == 'H':
		ptsHome = 3
	elif row['FTR'] == 'A':
		ptsAway = 3
	elif row['FTR'] == 'D':
		ptsHome = 1
		ptsAway = 1

	teamTracking[home]['pts'] += ptsHome
	teamTracking[home]['recent'].append(ptsHome)
	teamTracking[home]['recentHome'].append(ptsHome)

	teamTracking[away]['pts'] += ptsAway
	teamTracking[away]['recent'].append(ptsAway)
	teamTracking[away]['recentAway'].append(ptsAway)

###############
# Season 16/17
###############

df16_17_stats = df16_17.iloc[:,:23]


## 1) Points obtained until the match

squads_16_17 = (df16_17.HomeTeam.unique())

# create a new dataframe for controlling purposes

dct_16_17_pts = {}
for squad in squads_16_17:
	dct_16_17_pts[f'{squad}'] = []



for squad in squads_16_17:
	for line in df16_17_stats.iloc:
		if line["HomeTeam"] == squad:
			if line["FTR"] == "H":
				dct_16_17_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_16_17_pts[f'{squad}'].append(1)
			elif line["FTR"] == "A":
				dct_16_17_pts[f'{squad}'].append(0)

		if line["AwayTeam"] == squad:
			if line["FTR"] == "A":
				dct_16_17_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_16_17_pts[f'{squad}'].append(1)
			elif line["FTR"] == "H":
				dct_16_17_pts[f'{squad}'].append(0)




df_pts_16_17 = pd.DataFrame(dct_16_17_pts, columns = dct_16_17_pts.keys())


df16_17_stats["Home_cum_pts"] = np.nan
df16_17_stats["Away_cum_pts"] = np.nan



df_pts_16_17_cum = df_pts_16_17.apply(np.cumsum)
df_pts_16_17_xum_T = df_pts_16_17.transpose()


cols = df_pts_16_17.columns
col_team = list(cols)


## 2) scored goals until the match date


# create a new dataframe for controlling purposes

dct_16_17_goals = {}
for squad in squads_16_17:
	dct_16_17_goals[f'{squad}'] = []



for squad in squads_16_17:
	for line in df16_17_stats.iloc:
		if line["HomeTeam"] == squad:
			dct_16_17_goals[f'{squad}'].append(line["FTHG"])

		if line["AwayTeam"] == squad:
			dct_16_17_goals[f'{squad}'].append(line["FTAG"])



df_goals_16_17= pd.DataFrame(dct_16_17_goals, columns = dct_16_17_goals.keys())

df_goals_16_17 = df_goals_16_17.apply(np.cumsum)
df_goals_16_17_T = df_goals_16_17.transpose()

df16_17_stats["Home_cum_golas"] = np.nan
df16_17_stats["Away_cum_golas"] = np.nan

# Add the statistics to the main dataframe


teamTracking = defaultdict(lambda: { 'pts' : 0, 'games' : 0, 'goals':0,'goalsagainst':0, 'recent': [], 'recentHome': [], 'recentAway': []} )



# Add new columns
df16_17['PointsHome'] = ''
df16_17['PointsAway'] = ''
df16_17['GamesHome'] = ''
df16_17['GamesAway'] = ''
df16_17['GoalsHome'] = ''
df16_17['GoalsAway'] = ''
df16_17['GoalsagainstHome'] = ''
df16_17['GoalsagainstAway'] = ''



for n,row in df16_17.iterrows():

	home = row['HomeTeam']
	away = row['AwayTeam']

	# Write tracking data before altering
	df16_17.at[n, 'PointsHome'] = teamTracking[home]['pts']
	df16_17.at[n, 'PointsAway'] = teamTracking[away]['pts']
	df16_17.at[n, 'GamesHome'] = teamTracking[home]['games']
	df16_17.at[n, 'GamesAway'] = teamTracking[away]['games']
	df16_17.at[n, 'GoalsHome'] = teamTracking[home]['goals']
	df16_17.at[n, 'GoalsAway'] = teamTracking[away]['goals']
	df16_17.at[n, 'GoalsagainstHome'] = teamTracking[home]['goalsagainst']
	df16_17.at[n, 'GoalsagainstAway'] = teamTracking[away]['goalsagainst']


	# Update tracking data
	teamTracking[home]['games'] += 1
	teamTracking[away]['games'] += 1

	if row['FTR'] == 'H' :
		teamTracking[home]['pts'] += 3
	elif row['FTR'] == 'A' :
		teamTracking[away]['pts'] += 3
	elif row['FTR'] == 'D' :
		teamTracking[home]['pts'] += 1
		teamTracking[away]['pts'] += 1

	teamTracking[home]['goals'] += row['FTHG']
	teamTracking[away]['goals'] += row['FTAG']

	teamTracking[home]['goalsagainst'] += row['FTAG']
	teamTracking[away]['goalsagainst'] += row['FTHG']



# Write tracking data before altering
	df16_17.at[n, 'TotalLast5Home'] = sum(teamTracking[home]['recent'][-5:])
	df16_17.at[n, 'TotalLast5Away'] = sum(teamTracking[away]['recent'][-5:])
	df16_17.at[n, 'Last5WhenHome'] = sum(teamTracking[home]['recentHome'][-5:])
	df16_17.at[n, 'Last5WhenAway'] = sum(teamTracking[away]['recentAway'][-5:])



	ptsHome = 0
	ptsAway = 0
	if row['FTR'] == 'H':
		ptsHome = 3
	elif row['FTR'] == 'A':
		ptsAway = 3
	elif row['FTR'] == 'D':
		ptsHome = 1
		ptsAway = 1

	teamTracking[home]['pts'] += ptsHome
	teamTracking[home]['recent'].append(ptsHome)
	teamTracking[home]['recentHome'].append(ptsHome)

	teamTracking[away]['pts'] += ptsAway
	teamTracking[away]['recent'].append(ptsAway)
	teamTracking[away]['recentAway'].append(ptsAway)


###############
# Season 17/18
###############


df17_18_stats = df17_18.iloc[:,:23]


## 1) Points obtained until the match

squads_17_18 = (df17_18.HomeTeam.unique())

# create a new dataframe for controlling purposes

dct_17_18_pts = {}
for squad in squads_17_18:
	dct_17_18_pts[f'{squad}'] = []


for squad in squads_17_18:
	for line in df17_18_stats.iloc:
		if line["HomeTeam"] == squad:
			if line["FTR"] == "H":
				dct_17_18_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_17_18_pts[f'{squad}'].append(1)
			elif line["FTR"] == "A":
				dct_17_18_pts[f'{squad}'].append(0)

		if line["AwayTeam"] == squad:
			if line["FTR"] == "A":
				dct_17_18_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_17_18_pts[f'{squad}'].append(1)
			elif line["FTR"] == "H":
				dct_17_18_pts[f'{squad}'].append(0)




df_pts_17_18 = pd.DataFrame(dct_17_18_pts, columns = dct_17_18_pts.keys())


df17_18_stats["Home_cum_pts"] = np.nan
df17_18_stats["Away_cum_pts"] = np.nan



df_pts_17_18_cum = df_pts_17_18.apply(np.cumsum)
df_pts_17_18_xum_T = df_pts_17_18.transpose()


cols = df_pts_17_18.columns
col_team = list(cols)


## 2) Goals scored


# Create a new dataframe for controlling purposes

dct_17_18_goals = {}
for squad in squads_17_18:
	dct_17_18_goals[f'{squad}'] = []



for squad in squads_17_18:
	for line in df17_18_stats.iloc:
		if line["HomeTeam"] == squad:
			dct_17_18_goals[f'{squad}'].append(line["FTHG"])

		if line["AwayTeam"] == squad:
			dct_17_18_goals[f'{squad}'].append(line["FTAG"])



df_goals_17_18= pd.DataFrame(dct_17_18_goals, columns = dct_17_18_goals.keys())

df_goals_17_18 = df_goals_17_18.apply(np.cumsum)
df_goals_17_18_T = df_goals_17_18.transpose()

df17_18_stats["Home_cum_golas"] = np.nan
df17_18_stats["Away_cum_golas"] = np.nan

# Add the statistics to the main dataframe


teamTracking = defaultdict(lambda: { 'pts' : 0, 'games' : 0, 'goals':0,'goalsagainst':0, 'recent': [], 'recentHome': [], 'recentAway': []} )



# Add new columns
df17_18['PointsHome'] = ''
df17_18['PointsAway'] = ''
df17_18['GamesHome'] = ''
df17_18['GamesAway'] = ''
df17_18['GoalsHome'] = ''
df17_18['GoalsAway'] = ''
df17_18['GoalsagainstHome'] = ''
df17_18['GoalsagainstAway'] = ''


for n,row in df17_18.iterrows():

	home = row['HomeTeam']
	away = row['AwayTeam']

	# Write tracking data before altering
	df17_18.at[n, 'PointsHome'] = teamTracking[home]['pts']
	df17_18.at[n, 'PointsAway'] = teamTracking[away]['pts']
	df17_18.at[n, 'GamesHome'] = teamTracking[home]['games']
	df17_18.at[n, 'GamesAway'] = teamTracking[away]['games']
	df17_18.at[n, 'GoalsHome'] = teamTracking[home]['goals']
	df17_18.at[n, 'GoalsAway'] = teamTracking[away]['goals']
	df17_18.at[n, 'GoalsagainstHome'] = teamTracking[home]['goalsagainst']
	df17_18.at[n, 'GoalsagainstAway'] = teamTracking[away]['goalsagainst']


	# Update tracking data
	teamTracking[home]['games'] += 1
	teamTracking[away]['games'] += 1

	if row['FTR'] == 'H' :
		teamTracking[home]['pts'] += 3
	elif row['FTR'] == 'A' :
		teamTracking[away]['pts'] += 3
	elif row['FTR'] == 'D' :
		teamTracking[home]['pts'] += 1
		teamTracking[away]['pts'] += 1

	teamTracking[home]['goals'] += row['FTHG']
	teamTracking[away]['goals'] += row['FTAG']
	teamTracking[home]['goalsagainst'] += row['FTAG']
	teamTracking[away]['goalsagainst'] += row['FTHG']




# Write tracking data before altering
	df17_18.at[n, 'TotalLast5Home'] = sum(teamTracking[home]['recent'][-5:])
	df17_18.at[n, 'TotalLast5Away'] = sum(teamTracking[away]['recent'][-5:])
	df17_18.at[n, 'Last5WhenHome'] = sum(teamTracking[home]['recentHome'][-5:])
	df17_18.at[n, 'Last5WhenAway'] = sum(teamTracking[away]['recentAway'][-5:])



	ptsHome = 0
	ptsAway = 0
	if row['FTR'] == 'H':
		ptsHome = 3
	elif row['FTR'] == 'A':
		ptsAway = 3
	elif row['FTR'] == 'D':
		ptsHome = 1
		ptsAway = 1

	teamTracking[home]['pts'] += ptsHome
	teamTracking[home]['recent'].append(ptsHome)
	teamTracking[home]['recentHome'].append(ptsHome)

	teamTracking[away]['pts'] += ptsAway
	teamTracking[away]['recent'].append(ptsAway)
	teamTracking[away]['recentAway'].append(ptsAway)



###############
# Season 18/19
###############

df18_19_stats = df18_19.iloc[:,:23]


## 1) Points obtained until the match

# Create a new dataframe for controlling purposes

squads_18_19 = (df18_19.HomeTeam.unique())



dct_18_19_pts = {}
for squad in squads_18_19:
	dct_18_19_pts[f'{squad}'] = []



for squad in squads_18_19:
	for line in df18_19_stats.iloc:
		if line["HomeTeam"] == squad:
			if line["FTR"] == "H":
				dct_18_19_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_18_19_pts[f'{squad}'].append(1)
			elif line["FTR"] == "A":
				dct_18_19_pts[f'{squad}'].append(0)

		if line["AwayTeam"] == squad:
			if line["FTR"] == "A":
				dct_18_19_pts[f'{squad}'].append(3)
			elif line["FTR"] == "D":
				dct_18_19_pts[f'{squad}'].append(1)
			elif line["FTR"] == "H":
				dct_18_19_pts[f'{squad}'].append(0)




df_pts_18_19 = pd.DataFrame(dct_18_19_pts, columns = dct_18_19_pts.keys())


df18_19_stats["Home_cum_pts"] = np.nan
df18_19_stats["Away_cum_pts"] = np.nan



df_pts_18_19_cum = df_pts_18_19.apply(np.cumsum)
df_pts_18_19_xum_T = df_pts_18_19.transpose()


cols = df_pts_18_19.columns
col_team = list(cols)


## 2) Goals scored

# Create a new dataframe for controlling purposes

dct_18_19_goals = {}
for squad in squads_18_19:
	dct_18_19_goals[f'{squad}'] = []



for squad in squads_18_19:
	for line in df18_19_stats.iloc:
		if line["HomeTeam"] == squad:
			dct_18_19_goals[f'{squad}'].append(line["FTHG"])

		if line["AwayTeam"] == squad:
			dct_18_19_goals[f'{squad}'].append(line["FTAG"])



df_goals_18_19= pd.DataFrame(dct_18_19_goals, columns = dct_18_19_goals.keys())

df_goals_18_19 = df_goals_18_19.apply(np.cumsum)
df_goals_18_19_T = df_goals_18_19.transpose()

df18_19_stats["Home_cum_golas"] = np.nan
df18_19_stats["Away_cum_golas"] = np.nan


# Add the statistics to the main dataframe



teamTracking = defaultdict(lambda: { 'pts' : 0, 'games' : 0, 'goals':0,'goalsagainst':0, 'recent': [], 'recentHome': [], 'recentAway': []} )



# Add new columns
df18_19['PointsHome'] = ''
df18_19['PointsAway'] = ''
df18_19['GamesHome'] = ''
df18_19['GamesAway'] = ''
df18_19['GoalsHome'] = ''
df18_19['GoalsAway'] = ''
df18_19['GoalsagainstHome'] = ''
df18_19['GoalsagainstAway'] = ''


for n,row in df17_18.iterrows():

	home = row['HomeTeam']
	away = row['AwayTeam']

	# Write tracking data before altering
	df18_19.at[n, 'PointsHome'] = teamTracking[home]['pts']
	df18_19.at[n, 'PointsAway'] = teamTracking[away]['pts']
	df18_19.at[n, 'GamesHome'] = teamTracking[home]['games']
	df18_19.at[n, 'GamesAway'] = teamTracking[away]['games']
	df18_19.at[n, 'GoalsHome'] = teamTracking[home]['goals']
	df18_19.at[n, 'GoalsAway'] = teamTracking[away]['goals']
	df18_19.at[n, 'GoalsagainstHome'] = teamTracking[home]['goalsagainst']
	df18_19.at[n, 'GoalsagainstAway'] = teamTracking[away]['goalsagainst']


	# Update tracking data
	teamTracking[home]['games'] += 1
	teamTracking[away]['games'] += 1

	if row['FTR'] == 'H' :
		teamTracking[home]['pts'] += 3
	elif row['FTR'] == 'A' :
		teamTracking[away]['pts'] += 3
	elif row['FTR'] == 'D' :
		teamTracking[home]['pts'] += 1
		teamTracking[away]['pts'] += 1

	teamTracking[home]['goals'] += row['FTHG']
	teamTracking[away]['goals'] += row['FTAG']
	teamTracking[home]['goalsagainst'] += row['FTAG']
	teamTracking[away]['goalsagainst'] += row['FTHG']




# Write tracking data before altering
	df18_19.at[n, 'TotalLast5Home'] = sum(teamTracking[home]['recent'][-5:])
	df18_19.at[n, 'TotalLast5Away'] = sum(teamTracking[away]['recent'][-5:])
	df18_19.at[n, 'Last5WhenHome'] = sum(teamTracking[home]['recentHome'][-5:])
	df18_19.at[n, 'Last5WhenAway'] = sum(teamTracking[away]['recentAway'][-5:])



	ptsHome = 0
	ptsAway = 0
	if row['FTR'] == 'H':
		ptsHome = 3
	elif row['FTR'] == 'A':
		ptsAway = 3
	elif row['FTR'] == 'D':
		ptsHome = 1
		ptsAway = 1

	teamTracking[home]['pts'] += ptsHome
	teamTracking[home]['recent'].append(ptsHome)
	teamTracking[home]['recentHome'].append(ptsHome)

	teamTracking[away]['pts'] += ptsAway
	teamTracking[away]['recent'].append(ptsAway)
	teamTracking[away]['recentAway'].append(ptsAway)




###################################################################################################

##########################################################
# d) Merge all the seasons into one single final dataframe
##########################################################

df_total = pd.DataFrame(df14_15).append([df15_16, df16_17, df17_18, df18_19])

df_total['TotalLast5Home'] = df_total['TotalLast5Home'].astype(int)
df_total['TotalLast5Away'] = df_total['TotalLast5Away'].astype(int)
df_total['Last5WhenHome'] = df_total['Last5WhenHome'].astype(int)
df_total['Last5WhenAway'] = df_total['TotalLast5Away'].astype(int)
df_total['FTR'] = df_total['FTR'].replace(['H', 'D', 'A'], [0, 1, 2])

df_total.to_csv('df_final.csv', index=False)
