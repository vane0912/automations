from .Applications.Turkey.Turkey_evisa_180 import TR_App_P2
from .Applications.India.India_1y_Multiple import India_1y_Multiple
from .Applications.Egypt.Egypt_180_Multiple import EG_180_Multiple
automations_list = [
        {
            'Title': 'Turkey E-Visa 180 Days',
            'Country' : 'Turkey',
            'Type': TR_App_P2
        },
        {
            'Title': 'India 1 Year Multiple Entry',
            'Country' : 'India',
            'Type': India_1y_Multiple
        },
        {
            'Title': 'Visa Automation',
            'Country' : 'Egypt',
            'Type': EG_180_Multiple
        }
]