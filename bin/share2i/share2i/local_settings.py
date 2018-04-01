## -*- coding: utf-8 -*-
#Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '全员维修管理',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    #'MENU_EXCLUDE': ('auth.group','user'),
    'MENU': (
        # 'sites',
        {'app': 'auth.group'},
        {'app': 'user'},
        {'app': 'qrik_tools'},
        {'app': 'qrik_data'},
        {'app': 'qrik_auth','models':('App','Menu','Action',)},
        {'app': 'tpm_info','models':('Unit','EqpLevel','EqpType','Manufacturer','EqpClass','EqpModel','EqpOrg','EqpSection','EqpHost','EqpUnit','EqpPart','EqpHostExtend','EqpUnitExtend','EqpPartExtend',)},
        {'app': 'tpm_standard','models':('EqpStandard','SpotStandard','LubricationStandard','TastStandard',)},
        {'app': 'tpm_scheme','models':('SpotScheme','PreventiveScheme','FalutScheme',)},
        {'app': 'tpm_spot','models':('SpotPlan','SpotResource','SpotScheduling','SpotTask','SpotException','SpotTaskTrac',)},   
        {'app': 'tpm_preventive','models':('PreventivePlan','PreventiveResource','PreventiveScheduling','PreventiveTask','PreventiveTaskTrac',)},
        {'app': 'tpm_falut','models':('FalutConfirm','FalutPlan','FalutResource','FalutScheduling','FalutTask','FalutTaskTrac',)},  
        {'app': 'tpm_failure','models':('FailurePlan','FailureResource','FailureScheduling','FailureTask','FailureTaskTrac',)},            
        # {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        # {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),
    
    # misc
    'LIST_PER_PAGE': 15
}


URL_CATEGORY = {
"1":"1"
,"2":"2"
,"3":"3"
,"4":"4"
,"5":"5"
,"6":"6"
,"7":"7"
,"8":"8"
,"9":"9"
,"10":"10"
,"11":"11"
}



