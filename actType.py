# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 16:10:15 2015

@author: wu34
"""

#transportation1:
Type1 = ['walk']
#transportation2
Type2 = ['ov','car','bus','train','taxi','drive']
#transportaion3
Type3 = ['bike','cycle']
#work/study related
Type4 = ['craftwork','traineeship','exam','homework','read','work','lesson','sit','university','lecture','school','study']
#entertainment/relax:
Type5 = ['rest','relax','bed','shop','travel','watch','game','play','computer','tv','movie','jacuzzi','pub']
#social related
Type6 = ['activity','meet','friends','call','party','talk','phone','parent','visit']
#sport related
Type7 = ['run','sport','gym','hockey','swim','fitness','soccer','workout']
#others
Type8 = ['wait','household','pack','shower','clean','dress','toilet','babysitting']

def actType(word):
    act_type = 'none'
    if word in Type1:
        act_type = 'transportation1'
    if word in Type2:
        act_type = 'transportation2'
    if word in Type3:
        act_type = 'transportation3'
    if word in Type4:
        act_type = 'workStudy'
    if word in Type5:
        act_type = 'entertainmentRelax'
    if word in Type6:
        act_type = 'social'
    if word in Type7:
        act_type = 'sport'
    if word in Type8:
        act_type = 'others'
    return act_type 


