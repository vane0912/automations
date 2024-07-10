from .Applications.Turkey_evisa_180 import TR_App_P2
from .Applications.India_1y_Multiple import India_1y_Multiple
from .Applications.Egypt_180_Multiple import EG_180_Multiple

automations_list = [
        {
            'Title': 'Turkey-E-Visa-180-Days',
            'Subtitles': ['Only for MX citizens'],
            'Country' : 'Turkey',
            'Type': TR_App_P2,
            'Enabled': True,
            'Requirements': [
                {
                    'Label': 'ULR',
                    'Type': 'default',
                },
                {
                    'Label': 'Email',
                    'Type': 'default',
                },
                {
                    'Label': 'Status',
                    'Status_Available': ['Received', 'MIN']
                },
            ]
        },
        {
            'Title': 'India-1-Year-Multiple-Entry',
            'Subtitles': ['Only for MX citizens'],
            'Country' : 'India',
            'Type': India_1y_Multiple,
            'Enabled': True,
            'Requirements': [
                {
                    'Label': 'ULR',
                    'Type': 'default',
                },
                {
                    'Label': 'Email',
                    'Type': 'default',
                },
                {
                    'Label': 'Applicants',
                    'Type': 'Number',
                },
                {
                    'Label': 'Status',
                    'Status_Available': ['Received', 'Incomplete']
                },
                {
                    'Label': 'N. Orders',
                    'Type': 'Number',
                },
            ]
        },
        {
            'Title': 'Egypt-180-days-Multiple-Applicants',
            'Subtitles': ['Only for MX citizens'],
            'Country' : 'Egypt',
            'Type': EG_180_Multiple,
            'Enabled': False,
            'Requirements': [
                {
                    'Label': 'ULR',
                    'Type': 'default',
                },
                {
                    'Label': 'Email',
                    'Type': 'default',
                },
                {
                    'Label': 'Applicants',
                    'Type': 'default',
                },
                {
                    'Label': 'Status',
                    'Status_Available': ['Received', 'MIN']
                },
                {
                    'Label': 'N. Orders',
                    'Type': 'Number',
                },
                
            ]
        }
        
]