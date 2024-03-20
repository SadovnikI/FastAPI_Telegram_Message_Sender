from pydantic import BaseModel, field_validator, Field


class MessageData(BaseModel):
    bottoken: str = Field(..., description="Telegram Bot Token", example="1234567890:ABC_DEF1234567890")
    chatid: str = Field(..., description="Telegram Chat ID", example="123456789")
    message: str = Field(..., description="Message to be sent", example="Hello, world!")

    @field_validator('bottoken')
    @classmethod
    def validate_bottoken(cls, value: str):
        if len(value) > 46:  # Check if bottoken length <=46
            raise ValueError(f"Bot token must 46 characters or less long")
        return value
    @field_validator('chatid')
    @classmethod
    def validate_chatid_numeric(cls, value: str):
        if not value.isdigit():  # Check if chatid contains only numeric characters
            raise ValueError('Chat ID must contain only numeric characters')
        return value

    @field_validator('message')
    @classmethod
    def validate_message_length(cls, value):
        if len(value) > 4096:
            raise ValueError("Message length cannot exceed 4096 characters")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "bottoken": "1234567890:ABC_DEF1234567890",
                "chatid": "123456789",
                "message": "Hello, world!"
            }
        }
