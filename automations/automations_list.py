from .Applications.Turkey_evisa_180 import TR_App_P2
from .Applications.India_1y_Multiple import India_1y_Multiple
from .Applications.India_Business_eVisa import India_Business_eVisa
from .Applications.Egypt_180_Multiple import EG_180_Multiple
from .Applications.china_90_days import CHINA_90_DAYS
from .Applications.australia_visitor_visa import AUSTRALIA_VISITOR_VISA
from .Applications.oman_eVisa import OMAN_EVISA_30_DAYS
from .Applications.australia_eta import AUSTRALIA_ETA
from .Admin.check_orders_page import check_orders
from .Admin.doc_upload import doc_upload

automations_list_admin = [
    {
        'automation_id' : 1,
        'Title': 'Check-Orders-Page',
        'Subtitles': ['Customer orders and search pages can be viewed'],
        'Type': check_orders,
        'Enabled': True,
        'Requirements': [
                {
                    'Label': 'URL',
                    'Type': 'default',
                },
            ]
    },
    {
        'automation_id' : 2,
        'Title': 'Doc-Upload-Admin-Portal',
        'Subtitles': ['File Upload in the admin portal'],
        'Type': doc_upload,
        'Enabled': True,
        'Requirements': [
                {
                    'Label': 'URL',
                    'Type': 'default',
                },
            ]
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
                }
            ]
        },
        {
            'Title': 'China-Tourist-Visa-90-Days',
            'Subtitles': ['Only for MX citizens'],
            'Country' : 'China',
            'Type': CHINA_90_DAYS,
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
                    'Status_Available': ['Received', 'MIN']
                }
            ]
        },
        {
            'Title': 'India-1-Year-Multiple-Entry',
            'Subtitles': ['Only for US citizens'],
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
                    'Label': 'Status',
                    'Status_Available': ['Received', 'MIN']
                }
            ]
        },
        {
            'Title': 'Egypt-180-days-Multiple-Entries',
            'Subtitles': ['Only for US citizens'],
            'Country' : 'Egypt',
            'Type': EG_180_Multiple,
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
                }
            ]
        },
        {
            'Title': 'Australia-Visitor-Visa',
            'Subtitles': ['Only for MX citizens'],
            'Country' : 'Australia',
            'Type': AUSTRALIA_VISITOR_VISA,
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
                    'Status_Available': ['Received']
                }
            ]
        },
        {
            'Title': 'Australia-ETA',
            'Subtitles': ['Only for US citizens'],
            'Country' : 'Australia',
            'Type': AUSTRALIA_ETA,
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
                    'Status_Available': ['Received']
                }
            ]
        },
        {
            'Title': 'India-Business-eVisa',
            'Subtitles': ['Only for US citizens'],
            'Country' : 'India',
            'Type': India_Business_eVisa,
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
                }
            ]
        },
        {
            'Title': 'Oman-30-Days-Single-Entry',
            'Subtitles': ['Only for US citizens'],
            'Country' : 'Oman',
            'Type': OMAN_EVISA_30_DAYS,
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
                    'Status_Available': ['Received']
                },
                {
                    'Label': '',
                    'Type': 'default'
                }
            ]
        }
]