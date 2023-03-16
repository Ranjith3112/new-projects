notification =  {
                    "rulename": "TestRule",
                    "template": "testtemp",
                    "organization": [
                    "Ticvic",
                    "Infoquick"
                    ],
                    "communication_details": {
                    "email_configuration": {
                        "subject": "TestSubject",
                        "to_address": [
                        "sam@ticvic.com",
                        "raju@ticvic.com",
                        "guru@ticvic.com"
                        ],
                        "cc_address": [
                        "santhosh@ticvic.com",
                        "jayakkumar@ticvic.com",
                        "guru@ticvic.com"
                        ],
                        "message": "TestMessage"
                    },
                    "sms_configuration": {
                        "phone": +919980800502,
                        "text": "Test-SMS"
                    }
                    },
                    "conditions": [
                    {
                        "condition_name": "testone",
                        "condition_value": [
                        {
                            "attribute": "alarmtype",
                            "operator": "EQUALS",
                            "value": "login-auth-failed"
                            
                        },
                        {
                            "attribute": "alarmText",
                            "operator": "EQUALS",
                            "value": "login-auth-failed"
                            
                        }
                        ] 
                    },
                    {
                        "condition_name": "newTest",
                        "condition_value": [
                        {
                            "attribute": "deviceName",
                            "operator": "NOLIKE",
                            "value": "config-change"
                        },
                        {
                            "attribute": "deviceType",
                            "operator": "NOLIKE",
                            "value": "config-change"
                        }
                        ]
                    }
                    ]
                }
a = notification["communication_details"]["email_configuration"]["to_address"]
b = notification["communication_details"]["email_configuration"]["cc_address"]

for element in a:
    if element not in b:
        print(element)

print(notification["conditions"][0]["condition_name"])
print(notification["conditions"][0]["condition_value"])

# a =["Geeks", "for", "Geeks"]
# print(" ".join(a))


# import itertools as itr
# list1 = [1,2,3,4]

# prod = itr.product(list1, repeat=2)
# print(list(prod))