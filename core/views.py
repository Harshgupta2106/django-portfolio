from django.shortcuts import render

def home(request):
    context = {
        'name': 'Harsh Gupta',
        'role': 'Salesforce Developer | Python Enthusiast',
        'intro': 'Enthusiastic Salesforce Developer skilled in Apex, LWC, SOQL, and Flows with hands-on experience in building real-time CRM solutions. Passionate about scalable applications and automated workflows.',
        'trailhead_points': '39,000+',
        'experience': {
            'role': 'Salesforce Developer Intern',
            'company': 'Aazad Software Solutions',
            'duration': 'Feb 2026 - Present',
            'details': [
                'Developed LWC for member and transaction management modules.',
                'Implemented Apex classes and SOQL queries for dynamic data handling.',
                'Built reusable modal components and automated EMI reminder emails using Flows.'
            ]
        },
        'projects': [
            {
                'title': 'Society Loan & Contribution Management System',
                'tech': 'Salesforce CRM, Apex, LWC, Flow Builder',
                'desc': 'Financial management system for family contributions, EMI tracking, and dynamic dashboards with real-time refresh functionality.'
            }
        ],
        'skills': ['Apex', 'LWC', 'SOQL', 'Python', 'Django', 'JavaScript', 'Git']
    }
    return render(request, 'core/index.html', context)