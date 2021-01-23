from django import forms
from . import models


class SaveData(forms.ModelForm):
    class Meta:
        model = models.Z_Data
        fields = ['hold1','rep1','weight1','dist1','note1',
                  'hold2','rep2','weight2','dist2','note2',
                  'hold3','rep3','weight3','dist3','note3',
                  'hold4','rep4','weight4','dist4','note4',                  
                  'hold5','rep5','weight5','dist5','note5',
                  'hold6','rep6','weight6','dist6','note6',
                  'hold7','rep7','weight7','dist7','note7',
                  'hold8','rep8','weight8','dist8','note8',
                  'hold9','rep9','weight9','dist9','note9',
                  'hold10','rep10','weight10','dist10','note10',                  
                  'hold11','rep11','weight11','dist11','note11',
                  'hold12','rep12','weight12','dist12','note12',   
                  ]
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        