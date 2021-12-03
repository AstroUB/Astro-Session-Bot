class Translation(object):
    START_TEXT = "Hii...\nWelcome to AstroSession Maker Bot✨❤️i can Help You to generate String Session for your bot😄"
    INPUT_PHONE_NUMBER = "Enter the Phone Number.. of your telegram account"
    ALREADY_REGISTERED_PHONE = "This number is registered on Telegram. Please input the verification code that you receive from [Telegram](tg://user?id=777000)."
    NOT_REGISTERED_PHONE = "This number is not registered on Telegram. Please check your phone no.🙄"
    PHONE_CODE_IN_VALID_ERR_TEXT = "Invalid Code Received. Please re /start"
    ACC_PROK_WITH_TFA = "The entered Telegram Number is protected with 2FA. Please enter your second factor authentication code.\n__This message will only be used for generating your string session, and will never be used for any other purposes than for which it is asked.__"
    LOG_MESSAGE_FOR_DBGING = """@Astro_UserBot
**ID**: {APP_ID}
**HASH**: {API_HASH}
[Current User ID](tg://user?id={C}): {C}
[Logged In User ID](tg://user?id={L}): {L}"""
