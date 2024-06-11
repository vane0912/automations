from .Applications.Turkey_evisa_180 import TR_App_P2, Global_Variables
from .Applications.India_1y_Multiple import India_1y_Multiple
from .Applications.Egypt_180_Multiple import EG_180_Multiple
from .Applications.test import test

automations_list = [
        {
            'Title': 'Turkey E-Visa 180 Days',
            'Country' : 'Turkey',
            'Type': test,
            'Requirements': [
                {
                    'Label': 'Url',
                    'Type': 'text',
                },
                {
                    'Label': 'Email',
                    'Type': 'text',
                },
                {
                    'Label': 'Applicants',
                    'Type': 'text',
                },
                {
                    'Label': 'Status',
                    'Type': 'text',
                },
                {
                    'Label': 'Currency',
                    'Type': 'Number',
                },
                {
                    'Label': 'Number of Orders',
                    'Type': 'Number',
                }
            ]
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