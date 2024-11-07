#!/usr/bin/env python
# coding: utf-8

# # Arbeidskrav 1
# ### Sindre Grønvold, 2024 - 11. 06
# 
# ###### Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.

# In[130]:


# Antall km på et år.
Km_year = 10000


# In[131]:


# Forsikring.
El_bil = 5000
Bensin_bil = 7500


# In[132]:


# Trafikkforsikringsavgift er lik for begge biler på et år. (årlig):
year = 365
avgift = 8.38
Avgift_biler = avgift *year


# In[133]:


# Drivstkostnader 
Elbil_drivstkostnader = Km_year * 0.2 * 2

Bensinbil_drivskostnader = Km_year * 1


# In[134]:


# Bomavgift for Elbil.
Bom_el = Km_year * 0.1
# Bomavgift for bensin bil.
Bom_bensin = Km_year * 0.3


# In[135]:


# Totalkostnader per år.

# Elbil: 
Total_el = El_bil + Avgift_biler + Elbil_drivstkostnader + Bom_el

# Bensinbil
Total_bensin = Bensin_bil + Avgift_biler + Bensinbil_drivskostnader + Bom_bensin


# In[136]:


print("Total kostnad for bensinbil vil være på" ,Total_bensin, "," , "mens totalkostnaden på elbil er" ,Total_el)


# <h1> Jeg ville personlig gått for en elbil, da ville jeg ha spart nesten 10.000 kr.</h1>
