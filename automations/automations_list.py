from .Applications.Turkey_evisa_180 import TR_App_P2
from .Applications.India_1y_Multiple import India_1y_Multiple
from .Applications.Egypt_180_Multiple import EG_180_Multiple
from .Weekly.USPR import USPR_PASSPORT_RENEWAL
automations_list_weekly = [
    {
        'Title': 'USPR-Passport-Renewal',
        'Subtitles': ['Creates the 3 applications to check that USPR validations work'],
        'Type': USPR_PASSPORT_RENEWAL,
        'Enabled': True
    }
]
automations_list_applications = [
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
                    'Label': 'Status',
                    'Status_Available': ['Incomplete']
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