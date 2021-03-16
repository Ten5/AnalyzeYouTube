from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=sports&sp=EgIQAQ%253D%253D")

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')

links = [
"https://www.youtube.com/watch?v=szeXkBYq5HU",
"https://www.youtube.com/watch?v=UL2BY0NR0Eo",
"https://www.youtube.com/watch?v=L6JebqqZbMg",
"https://www.youtube.com/watch?v=ieAj3Emg7lg",
"https://www.youtube.com/watch?v=Fg2G_N0vFxA"
]

for i in user_data:
	links.append(i.get_attribute('href'))

print(len(links))

df_sports = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])

wait = WebDriverWait(driver, 10)
v_category = "Sports"
for x in links:
	driver.get(x)
	v_id = x.strip("https://www.youtube.com/watch?v=")
	v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text
	v_description =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
	df_sports.loc[len(df_sports)] = [v_id, v_title, v_description, v_category]

frames = [df_sports]
df_copy = pd.concat(frames, axis = 0, join = "outer", join_axes = None, ignore_index = True, keys = None, levels = None, names = None, verify_integrity = False, copy = True)




# Midway Results :: df_sports / df_copy
#            link                                              title                                        description category
# 0    zeXkBYq5HU                                                     booking/inquires: beachbunnymusic@gmail.com\n\...   Sports
# 1    UL2BY0NR0E                                                     I do these videos ever year or so, they are ba...   Sports
# 2   L6JebqqZbMg                                                     Diogo Jota sank his former club, but a serious...   Sports
# 3   ieAj3Emg7lg                                                     Arsenal claimed bragging rights in North Londo...   Sports
# 4   Fg2G_N0vFxA                                                     #LIVE : SPORTS ARENA NDANI YA WASAFI FM  - MAR...   Sports
# 5    zeXkBYq5HU                               Beach Bunny - Sports  booking/inquires: beachbunnymusic@gmail.com\n\...   Sports
# 6    UL2BY0NR0E                                                     I do these videos ever year or so, they are ba...   Sports
# 7   L6JebqqZbMg  Wolves v. Liverpool | PREMIER LEAGUE HIGHLIGHT...  Diogo Jota sank his former club, but a serious...   Sports
# 8   ieAj3Emg7lg                                                     Arsenal claimed bragging rights in North Londo...   Sports
# 9   Fg2G_N0vFxA                                                     #LIVE : SPORTS ARENA NDANI YA WASAFI FM  - MAR...   Sports
# 10   47OY3NSDaR                                                     (if any of the links don't work, check most re...   Sports
# 11     GkToO1eH                  Top 100 Best Sports Bloopers 2020  Watch the Top 100 best sports bloopers from 20...   Sports
# 12  8SZX4wmV1jU              Top 100 Sports Plays of the Year 2020  Mind Boggling Displays of Athleticism from the...   Sports
# 13   3m_DlYSJOA                                                     Greatest World Records in Sport History video ...   Sports
# 14  QjL7D33xpS4                                                     From the new album ‘Street Worms’ out 28th Sep...   Sports
# 15  dwV04XuiWq4                                                     Why play just one sport when you can play ALL ...   Sports
# 16  dW8J7_l8INY                                                     Craziest “Saving Lives” Moments in Sports Hist...   Sports
# 17  _XFzT9GMmw8                                                     Discord Server: https://discord.gg/98YJQff\nAr...   Sports
# 18  0n29H1x5o0A                                                     Smartest "1000 IQ Plays" in Sports History\nPl...   Sports
# 19   9Ffm_X-ppF                                                     Discord Server: https://discord.gg/98YJQff\nAr...   Sports
# 20  1_r0mhnxGN0                         20 MUST SEE SPORTS MOMENTS                         20 MUST SEE SPORTS MOMENTS   Sports
# 21     IMwbNnXI                                                     Both teams were left to rue their missed chanc...   Sports
# 22   nXVhxO7zjA                                                     #Compilation #DumbestPlays #SportsHistory\n\nS...   Sports
# 23   _6akkGVr2z                                                     CHEAPEST FIFA 21 COINS HERE!! 👉🏾 - http://bi...   Sports
# 24   _eaK4DIxB5  Top 100 Sports Plays of the Decade | 2010 - 20...  Check out the Top 100 plays of the decade wher...   Sports



# Cleaning using NLTK

# Building model

# Analyzing