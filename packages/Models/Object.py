from pydantic import BaseModel

class Object(BaseModel):
    prop1 : str
    prop2 : str
    model_config = \
            {
                "json_schema_extra": \
                {
                    "examples": \
                    [
                        {
                            "prop1": "prop"
                            ,"prop2": "prop"
                        }
                    ]
                }
            }
    pass