surveyTextPayload = """{
    "type": "AdaptiveCard",
    "padding": "none",
    "originator": "0eb3a855-e2d4-4bc9-8038-b22d614e4788",
    "body": [
        {
            "type": "Container",
            "style": "emphasis",
            "items": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "verticalContentAlignment": "Center",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "verticalContentAlignment": "Center",
                                    "horizontalAlignment": "Left",
                                    "text": "**SURVEY**"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Container",
            "padding": {
                "top": "none",
                "left": "default",
                "bottom": "default",
                "right": "default"
            },
            "items": [
                {
                    "type": "TextBlock",
                    "text": "**?**",
                    "wrap": true
                },
                {
                    "type": "Input.Text",
                    "id": "input3",
                    "isMultiline": true
                },
                {
                    "type": "ActionSet",
                    "actions": [
                        {
                            "type": "Action.Http",
                            "title": "Next",
                            "method": "POST",
                            "body": "?",
                            "url": "https://amcompose.azurewebsites.net/getsurveyquestion"
                        }
                    ]
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0"
}"""
