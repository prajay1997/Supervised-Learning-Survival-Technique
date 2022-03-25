### solution of Q1) of Survival Analysis.

import pandas as pd
import lifelines
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\praja\Desktop\Data Science\Supervised Learning Technique\Survival Analytics\Patient.csv")
data.info()
# drop the unwanted column which is nor useful for the analysis
data.drop(["PatientID"], axis =1 , inplace = True)
data.describe()

# followup is referring to time

T = data.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initialising the kaplanMeierFitter model 
kmf =  KaplanMeierFitter()


# Fitting KaplanMeierFitter model on Time and Events for death

kmf.fit(T, event_observed = data.Eventtype, label = "A") 
kmf.plot()
plt.title("Kaplan Meier estimates ")
plt.xlabel("followup in hr")
plt.ylabel("Survival")
plt.show()

# From the graph we can say that as we followup arly then survival probability is more 

###############################################################################33

# solution of Q2) ######################

import pandas as pd
import statistics
import lifelines
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\praja\Desktop\Data Science\Supervised Learning Technique\Survival Analytics\ECG_Surv.xlsx")
data.columns
data.drop(['name'], axis =1 , inplace = True)
data = data.rename(columns = { 'wallmotion-score': 'wallmotion_score','wallmotion-index':'wallmotion_index'})

a = data.describe()
data.isnull().sum()

data.fillna(data.median(), inplace = True)

data.isnull().sum()

# survival_time_hr is referring to time 

T = data.survival_time_hr

# Importing the KaplanMeierFitter model to fit the survival analysis

from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(T, event_observed= data.alive)

# Time-line estimations plot 
kmf.plot()
plt.title("Kaplan Meier estimates")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# From the above graph we can see that survival rate decreases as the time in hrs increases 
# The kaplan estimates 1 for intial hours following the treatment and it decreses to 0.65 after 40 hours.'


# Over Multiple groups 

mean_age = data.age.mean()
mean_age

# Applying KaplanMeierFitter model on survival time  and alive Events for the age above  mean age 
kmf.fit(T[data.age > data.age.mean()], data.alive[data.age > data.age.mean()], label='above 62')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and alive event for the age below mean age
kmf.fit(T[data.age < data.age.mean()], data.alive[data.age < data.age.mean()], label='age_below 62')
kmf.plot(ax=ax)
plt.title("Kaplan Meier estimates for age group")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# if the patient has the more than 62 age there is less chances of survival at the early stage and if he has the age below 62 so there rate of survival is more .

data.pericardialeffusion.value_counts()

# Applying KaplanMeierFitter model on survival time  and alive Events for the  pericardialeffusion' = 1
kmf.fit(T[data.pericardialeffusion==1], data.alive[data.pericardialeffusion==1], label='1')
ax = kmf.plot()


# Applying KaplanMeierFitter model on Time and alive event for the pericardialeffusion' = 0
kmf.fit(T[data.pericardialeffusion==0], data.alive[data.pericardialeffusion==0], label='0')
kmf.plot(ax=ax)
plt.title("Kaplan Meier estimates fo pericardialeffusion")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# If the patient has the pericardialenfussion issue then the rate of hazards happening is high compare to the patient 
# which don't have this issue.

x = data.fractionalshortening.mean()

# Applying KaplanMeierFitter model on survival time  and alive Events for fractionalshortening above mean value 
kmf.fit(T[data.fractionalshortening >  x], data.alive[data.fractionalshortening > x], label=' above 0.23')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and alive event for  fractionalshortening below mean value 
kmf.fit(T[data.fractionalshortening< x], data.alive[data.fractionalshortening < x], label='below 0.23')
kmf.plot(ax=ax)
plt.title("Kaplan Meier estimates for fractionalshortening")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()
# as we cans see from gtaph as the value is less for fractionalshortening  there is less chances of survival
#and as the value is more for fractionalshortening  there is more chances of survival

 y = data.epss.mean()

# Applying KaplanMeierFitter model on survival time  and alive Events for epss above mean value 
kmf.fit(T[data.epss > y], data.alive[data.epss > y], label='above 12')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and alive event for epss below mean value 
kmf.fit(T[data.epss < y], data.alive[data.epss < y], label='below 12')
kmf.plot(ax=ax)
plt.title("Kaplan Meier estimates fo epss")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# from the graph we can sat that the as the epss is high the rate of dander is high 
#a and the epss is less then the rate of dander is low.


z = data.lvdd.mean()
# Applying KaplanMeierFitter model on survival time  and alive Events for lvdd above mean value 
kmf.fit(T[data.lvdd > z], data.alive[data.lvdd > z], label='lvdd more')
ax = kmf.plot()
# Applying KaplanMeierFitter model on survival time  and alive Events for lvdd below  mean value 
kmf.fit(T[data.lvdd < z], data.alive[data.lvdd < z], label ='lvdd less')
kmf.plot(ax = ax)
plt.title("Kaplan Meier estimates for age lvdd")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# as lvdd is less then the rate of getting into danger is low and if lvdd is more then the rate of getting into dander is less 

w = data.wallmotion_score.mean()

# Applying KaplanMeierFitter model on survival time  and alive Events for wallmotion_score above mean value 
kmf.fit(T[data.wallmotion_score > w], data.alive[data.wallmotion_score > w], label='score more')
ax = kmf.plot()

# Applying KaplanMeierFitter model on survival time  and alive Events for lvdd below  mean value 
kmf.fit(T[data.wallmotion_score < w], data.alive[data.wallmotion_score < w], label ='score less')
kmf.plot(ax = ax)
plt.title("Kaplan Meier estimates for  wallmotion_score")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# as we can see from the graph wallmotion score is less then more chances of survive and if the score is more there is less chances of survival

 wi = data.wallmotion_index.mean()
# Applying KaplanMeierFitter model on survival time  and alive Events for wallmotion_index above mean value 
kmf.fit(T[data.wallmotion_index > wi], data.alive[data.wallmotion_index> wi], label ='wallmotion_index high')
ax = kmf.plot()

# Applying KaplanMeierFitter model on survival time  and alive Events for wallmotion_index below  mean value 
kmf.fit(T[data.wallmotion_index < wi], data.alive[data.wallmotion_index< wi], label ='wallmotion_index less')
kmf.plot(ax = ax)
plt.title("Kaplan Meier estimates for wallmotion_index")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# from the graph we can sat that as wallmotion index is high then the chances of survival is less  with time and if it is iess then then the chances is more with time 


m = data.multi_sensor.mean()
# Applying KaplanMeierFitter model on survival time  and alive Events for multi_sensor above mean value 
kmf.fit(T[data.multi_sensor > m], data.alive[data.multi_sensor> m], label ='multi_sensorhigh')
ax = kmf.plot()

# Applying KaplanMeierFitter model on survival time  and alive Events for multi_sensor below  mean value 
kmf.fit(T[data.multi_sensor < m], data.alive[data.multi_sensor< m], label ='multi_sensor less')
kmf.plot(ax = ax)
plt.title("Kaplan Meier estimates for multi_sensor")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# if multisensor is  less then chance of survival is less and if it is high the the chance of survavial is slightly more


data['group'].value_counts()
# Applying KaplanMeierFitter model on survival time  and alive Events for group =1
kmf.fit(T[data.group == 1], data.alive[data.group ==1 ], label = 'group1')
kmf.plot()

# Applying KaplanMeierFitter model on survival time  and alive Events for group =2
kmf.fit(T[data.group == 2 ], data.alive[data.group==2], label ='group2')
kmf.plot()

# applying kaplanMeierFitter model on survival time and alive events for group =3
kmf.fit(T[data.group == 3], data.alive[data.group==3],label = 'group3')
kmf.plot()
plt.title("Kaplan Meier estimates for group")
plt.xlabel("hrs after heart attack")
plt.ylabel("Survival")
plt.show()

# group1 patient has less chances of survival
# group2 has the little bit more chances of survival than group 1 
# group3 has less less probability upto 10hrs and after 10hrs the probality of survival decreases drastically and at 40th hr patient die.