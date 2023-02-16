from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators(object):
    """
    This class gather all locators from
    a screen in the dictionary way key-value to
    set android and/or ios locator
    """

    email_input = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/tetEmail'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeOther[`name == "emailTextReviewForLogin"`]/XCUIElementTypeStaticText[1]']
    }

    password_input = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/tetPassword'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeOther[`name == "passwrodTextReviewForLogin"`]/XCUIElementTypeStaticText[1]']
    }

    continue_btn = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/btnContinue'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Iniciar sesión"`]']
    }

    clear = {
        "android": [AppiumBy.ID, ''],
        "ios": [AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Borrar texto"]']
    }

    register_device_btn = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/btnRegisterDevice'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN, '']
    }

    input_code_device_validation = {
        "android": [AppiumBy.ID,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                    '.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx'
                    '.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.CheckedTextView['
                    '1]'],
        "ios": [AppiumBy.XPATH, '']
    }

    fingerprint_no_btn = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/btnNo'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN, '']
    }

    fingerprint_yes_btn = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/btnYes'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN, '']
    }

    crea_cuenta = {
        "android": [AppiumBy.ID, 'ai.powerup.stori.debug:id/tvSignUp'],
        "ios": [AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "¿No tienes cuenta? Crea una aquí"`]']
    }

