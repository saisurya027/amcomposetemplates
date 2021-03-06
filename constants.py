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
                    "text": "**%s**",
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
                            "body": "%s",
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
queryQuestionSurvey = "SELECT question FROM surveyquestion WHERE sid = %s"
queryTypeSurvey = "SELECT type FROM surveyquestion WHERE sid = %s"
UTF8 = "utf-8"
endCardSurvey = """{
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
                        "text": "**Thank You! Survey Ended**",
                        "wrap": true
                    }
                ]
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.0"
    } """
surveyTextCode = "1"
surveyNumericCode = "2"
surveyDateCode = "3"
surveyChoiceCode = "4"
surveyNumericPayload = """{
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
                    "text": "**%s**",
                    "wrap": true
                },
                {
                    "type": "Input.Number",
                    "id": "input3",
                    "placeholder": "enter a number",
                    "isMultiline": true
                },
                {
                    "type": "ActionSet",
                    "actions": [
                        {
                            "type": "Action.Http",
                            "title": "Next",
                            "method": "POST",
                            "body": "%s",
                            "url": "https://amcompose.azurewebsites.net/getsurveyquestion"
                        }
                    ]
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0"
} """
surveyDatePayload = """{
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
                    "text": "**%s**",
                    "wrap": true
                },
                {
                    "type": "Input.Date",
                    "id": "date"
                },
                {
                    "type": "ActionSet",
                    "actions": [
                        {
                            "type": "Action.Http",
                            "title": "Next",
                            "method": "POST",
                            "body": "%s",
                            "url": "https://amcompose.azurewebsites.net/getsurveyquestion"                        }
                    ]
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0"
}"""
choiceOptionWithComma = """{
                            "value": "%s",
                            "title": "%s"
                    },"""
choiceOptionWithoutComma = """{
                        "value": "%s",
                        "title": "%s"
                    }"""
surveyChoicePayload = """{
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
                    "text": "**%s**",
                    "wrap": true
                },
                {
                    "type": "Input.ChoiceSet",
                    "isMultiSelect": false,
                    "style": "expanded",
                    "choices": [ %s
                    ]
                    
                },
                {
                    "type": "ActionSet",
                    "actions": [
                        {
                            "type": "Action.Http",
                            "title": "Next",
                            "method": "POST",
                            "body": "%s",
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
sorryPayload = """{
    "type": "AdaptiveCard",
    "version": "1.0",
    "padding": "none",
    "originator": "863402fa-7924-43fa-a7e1-47293462aaf4",
    "body": [
        {
            "type": "Container",
            "style": "emphasis",
            "items": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "width": "32px",
                            "items": [
                                {
                                    "type": "Image",
                                    "width": "26px",
                                    "horizontalAlignment": "Center",
                                    "url": "data:image/png;base64,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",
                                    "altText": "Trello Logo"
                                }
                            ],
                            "type": "Column",
                            "style": null,
                            "backgroundImage": null,
                            "bleed": false
                        },
                        {
                            "width": "stretch",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Quick Poll",
                                    "size": "Large",
                                    "height": "stretch"
                                }
                            ],
                            "type": "Column",
                            "style": null,
                            "backgroundImage": null,
                            "bleed": false
                        }
                    ]
                }
            ]
        },
        {
            "type": "Container",
            "padding": {
                "left": "padding",
                "right": "padding",
                "bottom": "padding"
            },
            "items": [
                {
                    "text": "Sorry the poll has ended.",
                    "wrap": true,
                    "type": "TextBlock",
                    "size": "Large",
                    "separator": true
                }
            ]
        }
    ]
}"""
type = "type"
body = "body"
Container = "Container"
style = "style"
emphasis = "emphasis"
items = "items"
ColumnSet = "ColumnSet"
columns = "columns"
width = "width"
Column = "Column"
bleed = "bleed"
Image = "Image"
actions = "actions"
resources = "resources"
method = "method"
version = "version"
horizontalAlignment = "horizontalAlignment"
Logo = "data:image/png;base64,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"
bar = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAQCAYAAADj5tSrAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADeSURBVDhPtc1NCsIwEAXgWWrtj3oBb+ARvJl/bQU9hu5cegdXrhRc2IrYeggtgjwTmmCNKZJFFh/vEWYmVDwL2EabXQLbaDBcwzbqjbawjYIwgW3kRhfYRl50BueLlNxY37nqrLrnafbYJykrqRiWvcyq6tv3bF3/JDXjK0oZmjO1s6ztLGX/s8c+ubFSasz+dJ5Kd2RXZyudWmEGlRvlaDE86zrPr66544ikbpjjxzRDxwCf194RqD1JoArGJ2O6OxJ58z1U/uJgTHdHov7yCNto9XhBtbyb090pvfAGnMoj2pIEjCsAAAAASUVORK5CYII="
TextBlock = "TextBlock"
text = "text"
size = "size"
responsepayload = """{
        "type": "AdaptiveCard",
        "version": "1.0",
        "padding": "none",
        "originator": "863402fa-7924-43fa-a7e1-47293462aaf4",
        "body": [
            {
                "type": "Container",
                "style": "emphasis",
                "items": [
                    {
                        "type": "ColumnSet",
                        "columns": [
                            {
                                "width": "32px",
                                "items": [
                                    {
                                        "type": "Image",
                                        "width": "26px",
                                        "horizontalAlignment": "Center",
                                        "url": "data:image/png;base64,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",
                                        "altText": "Trello Logo"
                                    }
                                ],
                                "type": "Column",
                                "style": null,
                                "backgroundImage": null,
                                "bleed": false
                            },
                            {
                                "width": "stretch",
                                "items": [
                                    {
                                        "type": "TextBlock",
                                        "text": "Quick Poll",
                                        "size": "Large",
                                        "height": "stretch"
                                    }
                                ],
                                "type": "Column",
                                "style": null,
                                "backgroundImage": null,
                                "bleed": false
                            }
                        ]
                    }
                ]
            },
            {
                "type": "Container",
                "padding": {
                    "left": "padding",
                    "right": "padding",
                    "bottom": "padding"
                },
                "items": [
                    {
                        "text": "%s",
                        "wrap": true,
                        "type": "TextBlock",
                        "size": "Large",
                        "separator": true
                    },
                    {
                        "text": "Your Response: **%s**",
                        "wrap": true,
                        "type": "TextBlock",
                        "separator": true
                    }
                ]
            }
        ]
    }
        """
emailid = "meganB@M365x465174.onmicrosoft.com"
passwd = "mahgarg@2642"
emailSubject = "Responses Of Your Poll"
emailServer = "smtp.office365.com"
emailPort = 587
emailhtml = """\
    <html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <script type="application/adaptivecard+json">{
    "type": "AdaptiveCard",
    "version": "1.0",
    "originator": "863402fa-7924-43fa-a7e1-47293462aaf4",
    "hideOriginalBody": true,
    "body": [
      {
        "type": "TextBlock",
        "text": "Results Will be Displayed Soon..."
      }
    ],
    "autoInvokeAction": {
        "type": "Action.Http",
        "method": "POST",
        "hideCardOnInvoke": false,
        "url": "https://amcompose.azurewebsites.net/fetchLatestResponses",
        "body": "%s"
    }
  }
  </script>
</head>
</html>
    """
Originator = "863402fa-7924-43fa-a7e1-47293462aaf4"
textOriginator = "originator"