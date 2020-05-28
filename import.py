# This example a local file named 'final_emails.csv'
# This file contains a list of contact records to import.
# Each row in the file contains a column named "Company ID" that contains the companyId
# that the contact should be associated with.
import requests
import json
import os

post_url = 'http://api.hubapi.com/crm/v3/imports?hapikey=aaaa'

importRequest = {
    "name": "daily_import",
    "files": [
        {
            "fileName": "final_emails.csv",
            "fileImportPage": {
                "hasHeader": True,
                "columnMappings": [
                    {
                        "ignored": False,
                        "columnName": "Date Accepted onto Platform",
                        "idColumnType": None,
                        "propertyName": "influencer_application_date_accepted",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Influencer Application Decline Reason",
                        "idColumnType": None,
                        "propertyName": "influencer_application_decline_reason",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "influencer_application_referral",
                        "idColumnType": None,
                        "propertyName": "Influencer Application Referral",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Lead status",
                        "idColumnType": None,
                        "propertyName": "influencer_application_status",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Business Name",
                        "idColumnType": None,
                        "propertyName": "influencer_business_name",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Influencer Business Title",
                        "idColumnType": None,
                        "propertyName": "influencer_business_title",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "City",
                        "idColumnType": None,
                        "propertyName": "influencer_city",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Country/Region",
                        "idColumnType": None,
                        "propertyName": "influencer_country",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Influencer Email",
                        "idColumnType": "HUBSPOT_ALTERNATE_ID",
                        "propertyName": "influencer_email",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Influencer First Application Date",
                        "idColumnType": None,
                        "propertyName": "influencer_first_application_date",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Account rS ID",
                        "idColumnType": None,
                        "propertyName": "influencer_id",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Influencer IGS Segment",
                        "idColumnType": None,
                        "propertyName": "influencer_igs_segment",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Influencer Last Application Date",
                        "idColumnType": None,
                        "propertyName": "influencer_last_application_date",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Street address",
                        "idColumnType": None,
                        "propertyName": "influencer_mailing_address",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Name",
                        "idColumnType": None,
                        "propertyName": "influencer_name",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Phone number",
                        "idColumnType": None,
                        "propertyName": "influencer_phone",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "Postal Code",
                        "idColumnType": None,
                        "propertyName": "influencer_postal",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    },
                    {
                        "ignored": False,
                        "columnName": "State/Region",
                        "idColumnType": None,
                        "propertyName": "influencer_state",
                        "foreignKeyType": None,
                        "columnObjectType": "CONTACT",
                        "associationIdentifierColumn": False
                    }
                ]
            }
        }
    ]
}
