from notion_client import Client
import os
api_key = os.environ['NOTION_KEY']
notion = Client(auth=api_key)

database_id = "fdcfad677110425286d871c95575334f"

def create_job_application(company,position,stage="Applied"):
    new_page = {
    "Company": {
        "title": [
            {
                "text": {
                    "content": company 
                }
            }
        ]
    },
    "Stage": {
        "status": {
            "name": stage
        }
    },
    "Position": {
        "multi_select": [
            {
                "name": position
            }
        ]
    }
    }

    notion.pages.create(parent={"database_id": database_id}, properties=new_page)
    print("Success! Job application added.")

def have_already_applied(company,position):
    query_obj = {
        "database_id": database_id,
        "filter":{
            "and": [
                {
                    "property": "Company",
                    "title": {
                        "equals": company
                    }
                },
                {
                    "property": "Position",
                    "multi_select": {
                        "contains": position
                    }
                }
            ]
        }
    }
    

    results = notion.databases.query(**query_obj).get('results')
    if results:
        return True
    else:
        return False 

company = input('Company: ') 
position = input('Position: ')
if have_already_applied(company, position):
    print('You have already applied for that role')
else:
    create_job_application(company,position)